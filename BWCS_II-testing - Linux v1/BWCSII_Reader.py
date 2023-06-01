import platform
import threading
import time
import wx
import serial
import BWCSII_GUI
from pydispatch import dispatcher
import serial.tools.list_ports as ports
import os
import socket
from _thread import *
import struct

"""
class SERIALPORT_SCAN(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        dispatcher.connect(self.stop_thread, signal='stopscan', sender=dispatcher.Any)
        self.readExitFlag = 0

    def run(self):
        self.port_scan()

    def port_scan(self):
        while not self.readExitFlag:
            wx.CallAfter(dispatcher.send, "PortScan", None)
            time.sleep(0.5)
    def stop_thread(self):
        self.readExitFlag = 1
"""
class SOCKETSERVER(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        dispatcher.connect(self.stop_thread, signal="Close_Socket", sender=dispatcher.Any)
        self.readExitFlag = 0

    def run(self):
        self.socket_start()

    def socket_start(self):
        while not self.readExitFlag:
            wx.CallAfter(dispatcher.send, "ServerStart", None)
            time.sleep(5)

    def stop_thread(self):
        self.readExitFlag = 1


class TIMERUPDATE(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        dispatcher.connect(self.stop_thread, signal="StopTime", sender=dispatcher.Any)
        self.readExitFlag = 0

    # ------------------------------------------------------------------------------
    def run(self):
        self.time_read()

    # ------------------------------------------------------------------------------
    def time_read(self):
        while not self.readExitFlag:
            # dispatcher.send("SerialReceive", message=data)
            wx.CallAfter(dispatcher.send, "TimeReceive", time.ctime())  # Thread Safe method to transfer data
            time.sleep(0.1)

    # ------------------------------------------------------------------------------
    def stop_thread(self):
        """ Thread is stopped by this method """
        self.readExitFlag = 1


class SENSORREAD(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        dispatcher.connect(self.stop_thread, signal="StopSensor", sender=dispatcher.Any)
        self.readExitFlag = 0

    # ------------------------------------------------------------------------------
    def run(self):
        self.sensor_read()

    # ------------------------------------------------------------------------------
    def sensor_read(self):
        while not self.readExitFlag:
            # dispatcher.send("SerialReceive", message=data)
            wx.CallAfter(dispatcher.send, "SensorReceive", None)  # Thread Safe method to transfer data
            time.sleep(10)

    # ------------------------------------------------------------------------------
    def stop_thread(self):
        """ Thread is stopped by this method """
        self.readExitFlag = 1


class BWCSII(BWCSII_GUI.mainframe):
    def __init__(self, parent):
        BWCSII_GUI.mainframe.__init__(self, parent)
        icon = wx.Icon()
        wdir = os.getcwd()
        pltfom = platform.system()
        if pltfom.startswith('Linux'):
            icon.CopyFromBitmap(wx.Bitmap(wdir + "/cloud.png"))
        elif pltfom.startswith('Win'):
            icon.CopyFromBitmap(wx.Bitmap(wdir+"\\cloud.png"))
        self.SetIcon(icon)
        dispatcher.connect(self.time_display, signal="TimeReceive", sender=dispatcher.Any)
        self.timerThread = TIMERUPDATE()
        self.timerThread.start()
        dispatcher.connect(self.sensor, signal="SensorReceive", sender=dispatcher.Any)
        self.sensorThread = SENSORREAD()
        dispatcher.connect(self.accept_connections, signal="ServerStart", sender=dispatcher.Any)
        self.serverthread = SOCKETSERVER()
        COMs = ports.comports()
        for port, desc, hwid in sorted(COMs):
            self.comboBox_comList.Append(port)
        self.comboBox_comList.SetSelection(0)
        self.serialport = serial.Serial()
        self.skyTemp = 0
        self.ambTemp = 0
        self.humidity = 0
        self.windspeed = 0
        self.dewpoint = 0
        self.sensorSerialNo = '05198'
        self.FW_version = 'v73'
        self.rainStatus = 'N'
        self.sensorData = []
        self.logFile = ' '
        self.sht15_sensor_status = 0
        self.BWCSII_Connect = False
        if pltfom.startswith('Linux'):
            import fcntl
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.ipaddr = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', b'eth0'))[20:24])
        elif pltfom.startswith("Win"):
            host = socket.gethostname()
            self.ipaddr = socket.gethostbyname(host)
        self.port = 5050
        self.button_socketStatus.SetBackgroundColour('red')
        self.text_serverIP.SetLabel(str(self.ipaddr) + ':' + str(self.port))

    def button_portscan_OnClick( self, event ):
        self.comboBox_comList.Clear()
        COMs = ports.comports()
        for port, desc, hwid in sorted(COMs):
            self.comboBox_comList.Append(port)
        self.comboBox_comList.SetSelection(0)

    def time_display(self):
        cur_time = time.localtime()
        label = time.strftime('%A, %d %b %Y %H:%M:%S', cur_time)
        self.text_dateTime.SetLabel(label)
        if self.serialport.is_open:
            if not (self.logFile is time.strftime('Log_%Y%m%d.log')):
                self.logFile = time.strftime('Log_%Y%m%d.log')

    def mainFrame_OnClose(self, event):
        if self.timerThread.is_alive():
            dispatcher.send("StopTime")
        if self.sensorThread.is_alive():
            dispatcher.send("StopSensor")
        if self.serverthread.is_alive():
            if self.ServerSocket.connect_ex((self.ipaddr, self.port)):
                self.ServerSocket.close()
            dispatcher.send("Close_Socket")
        if self.serialport.is_open:
            self.serialport.close()
        self.Destroy()

    def button_exit_OnClick( self, event ):
        if self.timerThread.is_alive():
            dispatcher.send("StopTime")
        if self.sensorThread.is_alive():
            dispatcher.send("StopSensor")
        if self.serverthread.is_alive():
            if self.ServerSocket.connect_ex((self.ipaddr, self.port)):
                self.ServerSocket.close()
            dispatcher.send("Close_Socket")
        if self.serialport.is_open:
            self.serialport.close()
        self.Destroy()

    def button_comConnect_OnClick( self, event ):
        self.serialport.port = self.comboBox_comList.GetValue()
        self.serialport.baudrate = 4800
        self.serialport.timeout = 0
        self.serialport.bytesize = 8
        self.serialport.parity = serial.PARITY_NONE
        self.serialport.stopbits = serial.STOPBITS_ONE
        try:
            self.serialport.open()
        except:
            wx.MessageBox("Failed to open COM port", "WARNING", wx.ICON_WARNING)
        if self.serialport.isOpen():
            self.check_connection()
            if self.BWCSII_Connect:
                self.sensorThread.start()
                time.sleep(1)
                self.button_comConnect.SetBackgroundColour('Green')
                self.logFile = time.strftime('Log_%Y%m%d.log')
                self.sensor()
                self.button_comConnect.Disable()
                self.button_portscan.Disable()
            else:
                self.serialport.close()
                wx.MessageBox("Wrong port selected\nChange port and connect", "WARNING", wx.ICON_WARNING)

    def check_connection(self):
        cmd = 1
        self.serialport.write(chr(cmd).encode())
        time.sleep(5)
        for i in range(5):
            self.serialport.flush()
            line = self.serialport.readline()
            line = line.rstrip()
            line = line.lstrip(b'\x02P')
            if line.startswith(b'\x00\x02P'):
                line = line.lstrip(b'\x00\x02P')
            if line.startswith(b"MD") or line.startswith(b"MT") or line.startswith(b"MK") or line.startswith(b"MW") or line.startswith(b"MC"):
                self.BWCSII_Connect = True

    def update_display(self):
        #Sky temperature display
        if float(self.skyTemp) == -998.0:
            self.text_skyTemp.SetLabel('Sensor Wet')
            self.text_skyCondition.SetLabel('No Data')
        elif float(self.skyTemp) == 999.9:
            self.text_skyTemp.SetLabel('Saturated hot')
            self.text_skyCondition.SetLabel('No Data')
        elif float(self.skyTemp) == -999.9:
            self.text_skyTemp.SetLabel('Saturated Cold')
            self.text_skyCondition.SetLabel('No Data')
        else:
            self.text_skyTemp.SetLabel(str(self.skyTemp)+str(chr(176))+'C')
            if float(self.skyTemp) <= -32:
                self.text_skyCondition.SetLabel('Blue')
            elif (float(self.skyTemp) > -32) & (float(self.skyTemp) <= -25):
                self.text_skyCondition.SetLabel('Thin')
            elif (float(self.skyTemp) > -25) & (float(self.skyTemp) <= -20):
                self.text_skyCondition.SetLabel('Thick')
            elif (float(self.skyTemp) > -20) & (float(self.skyTemp) <= -15):
                self.text_skyCondition.SetLabel('V.Thick')
            elif (float(self.skyTemp) > -15) & (float(self.skyTemp) <= -10):
                self.text_skyCondition.SetLabel('Cloudy')
            else:
                self.text_skyCondition.SetLabel('V. Cloudy')

        #Humidity and Ambient temperature display
        if int(self.sht15_sensor_status) == 0:
            self.text_temperature.SetLabel(str(self.ambTemp)+str(chr(176))+'C')
            if int(self.humidity) <= 30:
                self.text_humCondition.SetLabel('Dry air')
            elif (int(self.humidity) > 30) & (int(self.humidity) < 55):
                self.text_humCondition.SetLabel('Good air')
            elif (int(self.humidity) >= 55) & (int(self.humidity) < 80):
                self.text_humCondition.SetLabel('Humid')
            else:
                self.text_humCondition.SetLabel('H. Humid')
            self.text_humidity.SetLabel(str(self.humidity)+'%')
        elif int(self.sht15_sensor_status) == 1:
            self.text_temperature.SetLabel(str(self.ambTemp) + str(chr(176)) + 'C')
            self.text_humidity.SetLabel('Failed')
        elif int(self.sht15_sensor_status) == 2:
            self.text_temperature.SetLabel(str(self.ambTemp) + str(chr(176)) + 'C')
            self.text_humidity.SetLabel('Waiting')
        elif int(self.sht15_sensor_status) == 3:
            if int(self.humidity) <= 30:
                self.text_humCondition.SetLabel('Dry air')
            elif (int(self.humidity) > 30) & (int(self.humidity) < 55):
                self.text_humCondition.SetLabel('Good air')
            elif (int(self.humidity) >= 55) & (int(self.humidity) < 80):
                self.text_humCondition.SetLabel('Humid')
            else:
                self.text_humCondition.SetLabel('H. Humid')
            self.text_humidity.SetLabel(str(self.humidity)+'%')
            self.text_temperature.SetLabel('Failed')
        elif int(self.sht15_sensor_status) == 4:
            if int(self.humidity) <= 30:
                self.text_humCondition.SetLabel('Dry air')
            elif (int(self.humidity) > 30) & (int(self.humidity) < 55):
                self.text_humCondition.SetLabel('Good air')
            elif (int(self.humidity) >= 55) & (int(self.humidity) < 80):
                self.text_humCondition.SetLabel('Humid')
            else:
                self.text_humCondition.SetLabel('H. Humid')
            self.text_humidity.SetLabel(str(self.humidity)+'%')
            self.text_temperature.SetLabel('Waiting')
        elif int(self.sht15_sensor_status) == 5:
            self.text_temperature.SetLabel(str(self.ambTemp) + str(chr(176)) + 'C')
            self.text_humidity.SetLabel('No Data')
        else:
            self.text_humidity.SetLabel(str(self.humidity) + '%')
            self.text_temperature.SetLabel('No Data')
        # Windspeed Data display
        if self.windspeed == '-1.0':
            self.text_windspeed.SetLabel('Heating Up')
            self.text_windCondition.SetLabel('No Data')
        elif self.windspeed == '-2.0':
            self.text_windspeed.SetLabel('Sensor Wet')
            self.text_windCondition.SetLabel('No Data')
        elif self.windspeed == '-3.0':
            self.text_windspeed.SetLabel('Bad sensor')
            self.text_windCondition.SetLabel('No Data')
        elif self.windspeed == '-4.0':
            self.text_windspeed.SetLabel('Not Heating')
            self.text_windCondition.SetLabel('No Data')
        else:
            self.text_windspeed.SetLabel(str(self.windspeed)+'Km/h')
            if float(self.windspeed) < 1:
                self.text_windCondition.SetLabel('Calm')
            elif (float(self.windspeed) >= 1) & (float(self.windspeed) < 2.5):
                self.text_windCondition.SetLabel('Breeze')
            elif (float(self.windspeed) >= 3.5) & (float(self.windspeed) < 9):
                self.text_windCondition.SetLabel('Windy')
            else:
                self.text_windCondition.SetLabel('H. Wind')

        #Dew point display
        self.text_dewpoint.SetLabel(str(self.dewpoint)+str(chr(176))+'C')

        #Rain status
        if self.rainStatus == 'N':
            self.text_rainCondition.SetLabel('No Rain')
        elif self.rainStatus == 'R':
            self.text_rainCondition.SetLabel('Raining')
        else:
            self.text_rainCondition.SetLabel('Raining')

        #Sensor seiral number and firmware details
        self.text_serialNum.SetLabel(self.sensorSerialNo)
        self.text_firmwareVer.SetLabel(self.FW_version)

    def sensor(self):
        cmd = 1
        self.serialport.write(chr(cmd).encode())
        time.sleep(0.5)
        for i in range(5):
            self.serialport.flush()
            line = self.serialport.readline()
            line = line.rstrip()
            line = line.lstrip(b'\x02P')
            if line.startswith(b'\x00\x02P'):
                line = line.lstrip(b'\x00\x02P')
            if line.startswith(b"MD") & ((len(line) < 160) & (len(line)>155)):
              #  print(str(line) + str(len(line)))
                data = str(line)
                self.sensorData.append(data)
                file = open(self.logFile, 'a')
                file.writelines(time.strftime("%H:%M:%S ") + data.lstrip("b'").rstrip("'")+'\n')
                file.close()
                self.read_D_data(data)
                line = ' '
            elif line.startswith(b"MT"):
               # print(str(line) + str(len(line)))
                data = str(line)
                self.sensorData.append(data)
                file = open(self.logFile, 'a')
                file.writelines(time.strftime("%H:%M:%S ") + data.lstrip("b'").rstrip("'")+'\n')
                file.close()
                #self.read_T_data(line)
                line = ' '
            elif line.startswith(b"MK"):
                #print(str(line) + str(len(line)))
                data = str(line)
                self.sensorData.append(data)
                file = open(self.logFile, 'a')
                file.writelines(time.strftime("%H:%M:%S ") + data.lstrip("b'").rstrip("'")+'\n')
                file.close()
               # self.read_K_data(line)
                line = ' '
            elif line.startswith(b"MW"):
                #print(str(line) + str(len(line)))
                data = str(line)
                self.sensorData.append(data)
                file = open(self.logFile, 'a')
                file.writelines(time.strftime("%H:%M:%S ") + data.lstrip("b'").rstrip("'")+'\n')
                file.close()
             #   self.read_W_data(line)
                line = ' '
            elif line.startswith(b"MC"):
                #print(str(line) + str(len(line)))
                data = str(line)
                self.sensorData.append(data)
                file = open(self.logFile, 'a')
                file.writelines(time.strftime("%H:%M:%S ") + data.lstrip("b'").rstrip("'")+'\n')
                file.close()
              #  self.read_C_data(line)
                line = ' '
            else:
                pass
            self.update_display()

    def read_D_data(self, line):
        line = line.lstrip("b'MD'")
        if "b'MD'" in line:
            data = line.split("b'MD'")[1]
            data = data.split()
        else:
            data = line.split()
        #print(data)
        self.sht15_sensor_status = data[0]
        self.skyTemp = data[6]
        self.ambTemp = data[7]
        self.windspeed = data[8]
        self.humidity = data[11]
        self.rainStatus = data[10]
        self.dewpoint = data[12]

    def read_T_data(self, line):
        line = line.lstrip('b"MT"')
        if "b'MT'" in line:
            data = line.split("b'MT'")[1]
            data = data.split()
        else:
            data = line.split()
        self.sensorSerialNo = data[0]
        self.FW_version = data[1]

#    def read_W_data(self, line):

 #   def read_K_data(self, line):

  #  def read_C_data(self):

    def button_StartSocket_OnClick( self, event ):
        self.ServerSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ServerSocket.settimeout(0.2)
        try:
            self.ServerSocket.bind((self.ipaddr, self.port))
        except socket.error as e:
            wx.MessageBox("Server start failed\n"+str(e), "WARNING", wx.ICON_WARNING)
        self.button_socketStatus.SetBackgroundColour('green')
        self.serverthread.start()
        self.button_StartSocket.Disable()

    def accept_connections(self):
        self.ServerSocket.listen()
        try:
            client, address = self.ServerSocket.accept()
        except socket.timeout:
            pass
        except:
            raise
        else:
        #with client:
            start_new_thread(self.client_handler, (client, ))

    def client_handler(self, connection):
        connection.send(str.encode('Server Connected'))
        while True:
            handshake = connection.recv(2048)
            msg = handshake.decode('utf-8')
            print(msg)
            if msg == 'BYE':
                break
            elif msg == 'Req_data':
                reply = f'{time.strftime("%H:%M:%S "), self.sensorSerialNo, self.FW_version, self.ambTemp, self.skyTemp, self.humidity, self.windspeed, self.dewpoint, self.sht15_sensor_status}'
                connection.send(str.encode(reply))
            else:
                pass
        connection.close()


if __name__ == "__main__":
    app = wx.App(False)

    GUI = BWCSII(None)

    GUI.Show(True)

    app.MainLoop()
