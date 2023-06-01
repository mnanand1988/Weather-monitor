import serial
import time
import serial.tools.list_ports as ports

serial_port = "COM3"
baudrate = 4800
timeout = 0
blocksize = 1000
databits = serial.EIGHTBITS
parity = serial.PARITY_NONE
stopbit = serial.STOPBITS_ONE

BWCSII = serial.Serial()
COMs = ports.comports()
for port, desc, hwid in sorted(COMs):
        print("{}: {} [{}]".format(port, desc, hwid))

BWCSII.port = serial_port
BWCSII.baudrate = baudrate
BWCSII.bytesize = databits
BWCSII.parity = parity
BWCSII.timeout = timeout

try:
    BWCSII.open()
except:
    print("COM3 open failed")
    exit(0)
cmd = 1
cnt = 1
while BWCSII.isOpen():
    BWCSII.write(chr(cmd).encode())
    time.sleep(0.5)
    #print(BWCSII.read())
    for i in range(5):
        BWCSII.flush()
        line = BWCSII.readline()
        line = line.rstrip()
        line = line.lstrip(b'\x02P')
        if line.startswith(b'\x00\x02P'):
            line = line.lstrip(b'\x00\x02P')

        if line.startswith(b"MD") & (len(line) == 159):
            print(str(cnt) + str(line) + str(len(line)))
            cnt = cnt + 1
            line = ' '
        elif line.startswith(b"MT"):
            print(str(cnt) + str(line) + str(len(line)))
            cnt = cnt + 1
            line = ' '
        elif line.startswith(b"MK"):
            print(str(cnt) + str(line)+ str(len(line)))
            cnt = cnt + 1
            line = ' '
        elif line.startswith(b"MW"):
            print(str(cnt) + str(line)+ str(len(line)))
            cnt = cnt + 1
            line = ' '
        elif line.startswith(b"MC"):
            print(str(cnt) + str(line)+ str(len(line)))
            cnt = cnt + 1
            line = ' '
        else:
            pass
        if cnt == 150:
            exit(0)

        """
       # val = val + str(line)
        if (len(line) == 0):
            pass
        elif (line == 'P'):
            pass
        else:
            print(str(cnt) + str(line))
            cnt = cnt+1
"""