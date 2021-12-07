import serial
opencr = serial.Serial(port = "/dev/ttyACM1",baudrate = 115200,timeout = 1  )

while True :
    number = input("enter a number:")
    opencr.write(bytes(number, "utf-8"))
    value = opencr.readline()
    print("Result:", value)
