
import serial
import cv2

def openOpencr():
    opencr = serial.Serial(port="/dev/ttyACM1", baudrate=115200, timeout=1)
    return opencr

def takeInput():
    key=cv2.waitKeyEx(1)
    if key > -1:
        print('key : ', key)
    return key

def runSerial(opencr):
    while True:
        img = cv2.imread('./kyung_jin.jpeg')
        cv2.imshow('robot_control',img) #keyboard input을 받기 위해 
        key= cv2.waitKeyEx(10)
        if key > -1:
            print('key : ', key, chr(key))

        if key == 27:
            break
        if key != -1:
            # opencr.write(bytes(num, 'utf-8'))
            opencr.write(bytes(chr(key), 'ascii'))

if __name__ == '__main__':
   
   try:
      opencrIns = openOpencr()
      if opencrIns != None:
          runSerial(opencrIns)
   except Exception as e:
      print(e)