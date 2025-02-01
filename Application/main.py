import serial

# for Linux users, change this to the appropriate COM port on windows
ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 115200

while True:
    # if there is no newline, this is fucked.
    print(ser.readline())
