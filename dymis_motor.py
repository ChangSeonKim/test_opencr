import serial
opencr = serial.Serial(port = "/dev/ttyACM0",baudrate = 115200,timeout = 1  )

while True :
    str = input("enter a number:")
    opencr.write(bytes(str, "utf-8"))
    value = opencr.readline()
    print("Result:", value)
