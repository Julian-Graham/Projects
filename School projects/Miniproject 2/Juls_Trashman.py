import RPi.GPIO as GPIO
import numpy as np
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
Echo_pin=12
Trig_pin=10
servo=3
LED=5
pulse_receive=0
pulse_start=0
GPIO.setup(Trig_pin,GPIO.OUT)
GPIO.setup(Echo_pin,GPIO.IN)
GPIO.output(Trig_pin,GPIO.LOW)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.LOW)
GPIO.setup(servo,GPIO.OUT)
p=GPIO.PWM(servo,50)
p.start(0)
while True:
    GPIO.output(Trig_pin,GPIO.LOW)
    time.sleep(.2)
    GPIO.output(Trig_pin,GPIO.HIGH)
    time.sleep(.00001)
    GPIO.output(Trig_pin,GPIO.LOW)
    while GPIO.input(Echo_pin)==0:
        pulse_start=time.time()
    while GPIO.input(Echo_pin)==1:
        pulse_receive=time.time()
    pulse_duration=pulse_receive-pulse_start
    distance=34000*pulse_duration/2
    print(distance , " cm away")
    time.sleep(0.1)
    if distance<15:
        GPIO.output(LED,True)
        for cycle in np.arange(2,5,3):
            p.ChangeDutyCycle(cycle)
            time.sleep(1)
        for cycle in np.arange(5,2,-3):
            p.ChangeDutyCycle(cycle)
            time.sleep(.3)
        GPIO.output(LED,False)
        p.ChangeDutyCycle(0)
