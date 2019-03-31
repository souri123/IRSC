import RPi.GPIO as IO
import time

import sys
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(19,IO.OUT)#TX Front
IO.setup(26,IO.IN)#RX Front


IO.setup(21,IO.OUT)#Buzzer output
IO.setup(13, IO.OUT) #PWM output

Motor1A = 17
Motor1B =27
distance_range =20
distance_range2 =15


IO.setup(Motor1A,IO.OUT)
IO.setup(Motor1B,IO.OUT)
dc=0  
pwm = IO.PWM(13, 100)
pwm.start(dc)

sensorFront_center_rx=26
sensorFront_center_tx=19

buzzer=21


def cont():
    #while(True):
        IO.output(Motor1A,IO.HIGH)
        IO.output(Motor1B,IO.HIGH)
        
        pwm.ChangeDutyCycle(80)
        time.sleep(1)
       


def stop():
    #while(True):
        IO.output(Motor1A,IO.HIGH)
        IO.output(Motor1B,IO.HIGH)
        
        pwm.ChangeDutyCycle(0)
        time.sleep(1)
       
        IO.output(buzzer,True)
        time.sleep(.1)
        IO.output(buzzer,False)
def slow():
    #while(True):
        IO.output(Motor1A,IO.HIGH)
        IO.output(Motor1B,IO.HIGH)
        for dc in range(65, 50, -20):
            pwm.ChangeDutyCycle(40)
            time.sleep(1)
            IO.output(buzzer,True)
            time.sleep(.5)
            IO.output(buzzer,False)
def frontCenter(sensorFront_center_rx,sensorFront_center_tx,buzzer):
    IO.output(sensorFront_center_tx, False)
    time.sleep(0.1)
    IO.output(sensorFront_center_tx, True)
    time.sleep(0.00001)
    IO.output(sensorFront_center_tx, False)
    while(IO.input(sensorFront_center_rx) == 0):
        pulse_start = time.time() 
    while(IO.input(sensorFront_center_rx) == 1):
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    print(distance)
    if distance < 30 and distance > 11:
        
        slow()
        
    elif distance < 10:
        stop()
    else:
        cont()

while(True):
   
    frontCenter(sensorFront_center_rx,sensorFront_center_tx,buzzer)
