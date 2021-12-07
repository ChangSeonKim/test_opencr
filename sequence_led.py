import serial
Arduino = serial.Serial(port = "/dev/ttyACM1",baudrate = 9600,timeout = None  )

while True :
    Arduino.pinMode(22, Arduino.INPUT)
    # opencr.write(bytes(number, "utf-8"))
    # value = opencr.readline()
    # print("Result:", value)
