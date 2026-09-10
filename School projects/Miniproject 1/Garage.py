import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
garage_servo=3
IR_1=5
IR_2=7
LED=11
GPIO.setup(IR_1,GPIO.IN)
GPIO.setup(IR_2,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,False)
GPIO.setup(garage_servo,GPIO.OUT)
p=GPIO.PWM(garage_servo,50)
p.start(0)
def open_garage():
    print("Place RFID tag to open")
    id,text=reader.read()
    if id==660795739126:
        print("Open sesame")
        if GPIO.input(IR_1):
            GPIO.output(LED,True)
            p.ChangeDutyCycle(6)
            while GPIO.input(IR_1)==1:
                time.sleep(.2)
            p.ChangeDutyCycle(7)
def close_garage():
    alloted_time=4
    start_time=time.time()
    print("Place RFID tag to close")
    id,text=reader.read()
    if id==660795739126:
        print("Bye bye")
        if GPIO.input(IR_2):
            GPIO.output(LED,True)
            p.ChangeDutyCycle(8)
            while GPIO.input(IR_2)==1:
                time.sleep(.2)
            p.ChangeDutyCycle(7)
            GPIO.output(LED,False)
    if time.time()>=alloted_time:
        print("You forgot to close. Auto closing")
        if GPIO.input(IR_2):
            GPIO.output(LED,True)
            p.ChangeDutyCycle(8)
            while GPIO.input(IR_2)==1:
                time.sleep(.2)
            p.ChangeDutyCycle(7)
            GPIO.output(LED,False)

    
while True:
    open_garage()
    close_garage()
        

