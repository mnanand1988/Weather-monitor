import platform
import threading
import time
import wx
import BWCSII_GUI
from pydispatch import dispatcher
import os
import socket


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


class SOCKETRREAD(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        dispatcher.connect(self.stop_thread, signal="StopSocket", sender=dispatcher.Any)
        self.readExitFlag = 0

    # ------------------------------------------------------------------------------
    def run(self):
        self.sensor_read()

    # ------------------------------------------------------------------------------
    def sensor_read(self):
        while not self.readExitFlag:
            # dispatcher.send("SerialReceive", message=data)
            wx.CallAfter(dispatcher.send, "SocketRead", None)  # Thread Safe method to transfer data
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
        dispatcher.connect(self.req_data, signal="SocketRead", sender=dispatcher.Any)
        self.socketread = SOCKETRREAD()
        self.skyTemp = 0
        self.ambTemp = 0
        self.humidity = 0
        self.windspeed = 0
        self.dewpoint = 0
        self.lastUpdate = ' '
        self.sht15_sensor_status = 0
        self.sensorSerialNo = '05198'
        self.FW_version = 'v73'
        self.rainStatus = 'N'
        self.host_ip = '192.168.30.5'
        self.host_port = 5050
        self.button_socketStatus.SetBackgroundColour('red')
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.text_lastUpdate.SetLabel("Default server: 192.168.30.5:5050")

    def time_display(self):
        cur_time = time.localtime()
        label = time.strftime('%A, %d %b %Y %H:%M:%S', cur_time)
        self.text_dateTime.SetLabel(label)

    def mainFrame_OnClose(self, event):
        if self.timerThread.is_alive():
            dispatcher.send("StopTime")
        if self.socketread.is_alive():
            if self.client.connect_ex((self.host_ip, self.host_port)):
                self.client.close()
            dispatcher.send("StopSocket")
        self.Destroy()

    def button_exit_OnClick(self, event):
        if self.timerThread.is_alive():
            dispatcher.send("StopTime")
        if self.socketread.is_alive():
            if self.client.connect_ex((self.host_ip, self.host_port)):
                self.client.close()
            dispatcher.send("StopSocket")
        self.Destroy()

    def validate_ip(self):
        try:
            socket.inet_aton(self.host_ip)
            if str(self.host_ip).startswith('192.168.'):
                return True
            else:
                wx.MessageBox("Invalid IP address, please enter a valid local IP\n eg: 192.168.30.5")
        except socket.error as e:
            wx.MessageBox("Invalid IP address\n" + str(e), "WARNING", wx.ICON_WARNING)
            return False

    def button_comConnect_OnClick(self, event):
        self.host_ip = str(self.text_host_IP.GetValue())
        self.host_port = int(self.text_host_portNo.GetValue())
        if self.validate_ip():
            try:
                self.client.connect((self.host_ip, self.host_port))
            except socket.error as e:
                wx.MessageBox("Server connection error\n" + str(e), "WARNING", wx.ICON_WARNING)
                return
            handshake = self.client.recv(1024)
            msg = handshake.decode('utf-8')
            if msg == "Server Connected":
                self.text_lastUpdate.SetLabel("Waiting for data...")
                self.button_socketStatus.SetBackgroundColour('green')
                self.button_comConnect.Disable()
                self.socketread.start()

    def req_data(self):
        self.client.send(str.encode("Req_data"))
        resp = self.client.recv(2048)
        resp = resp.decode("utf-8")
        resp = resp.rstrip(')')
        resp = resp.lstrip('(')
        data = resp.split(',')
       # print(data)
        self.sensorSerialNo = data[1].lstrip(" '").rstrip("'")
        self.FW_version = data[2].lstrip(" '").rstrip("'")
        self.ambTemp = data[3].lstrip(" '").rstrip("'")
        self.skyTemp = data[4].lstrip(" '").rstrip("'")
        self.humidity = data[5].lstrip(" '").rstrip("'")
        self.windspeed = data[6].lstrip(" '").rstrip("'")
        self.dewpoint = data[7].lstrip(" '").rstrip("'")
        self.lastUpdate = data[0].lstrip(" '").rstrip("'")
        self.sht15_sensor_status = data[8].lstrip(" '").rstrip("'")
        self.update_display()

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
        self.text_lastUpdate.SetLabel(self.lastUpdate)


if __name__ == "__main__":
    app = wx.App(False)

    GUI = BWCSII(None)

    GUI.Show(True)

    app.MainLoop()
