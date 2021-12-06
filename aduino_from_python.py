import serial
opencr = serial.Serial(port = "/dev/ttyACM0",baudrate = 115200,timeout = 1  )

while True :
    input("enter a number:")
    opencr.write(bytes(number, "utf-8"))
    value = opencr.readline()
    print("Result:", value)
# 20이상이면 뺄셈
#