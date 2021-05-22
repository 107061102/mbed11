import serial
import time

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)


print("start sending RPC")
while True:
    # send RPC to remote
    s.write("/AC/run 1\r".encode())
    time.sleep(1)


s.close()