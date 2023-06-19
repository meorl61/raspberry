#!/usr/bin/python3

  
from time import sleep     # this lets us have a time delay (see line 12)
import random

import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme.  


#設定PIN腳  
GPIO.setup(17, GPIO.OUT)# set GPIO 17 as output for blue led  
GPIO.setup(27, GPIO.OUT)# set GPIO 27 as output for green led  
GPIO.setup(22, GPIO.OUT)# set GPIO 22 as output for red led

hz = 75 
#hz = input('Please define the frequency in Herz(recommended:75): ')
#reddc = input('Please define the red LED Duty Cycle: ')
#greendc = input('Please define the green LED Duty Cycle: ')
#bluedc = input('Please define the blue LED Duty Cycle: ')

blue = GPIO.PWM(17, hz)    # create object red for PWM on port 17  
green = GPIO.PWM(27, hz)      # create object green for PWM on port 27   
red = GPIO.PWM(22, hz)      # create object blue for PWM on port 22 
sleeptime = 0.3
try:   
        i=15
        while True:
            red.start(random.randint(0,50))
            green.start(random.randint(0,50))
            blue.start(random.randint(0,50))
            sleep(sleeptime)
            #if(i<35):
            #    i+=1
            #else:
             #   i=0
            
            
            # red.start(i) # 紅reddc  start red led
            # sleep(sleeptime)                 # wait 0.5 seconds
 
            # red.start(i*2)
            # green.start(i*0.8) # greendc start green led
            # sleep(sleeptime)                 # wait 0.5 seconds
 
            # red.start(i*1)
            # green.start(i*1) # greendc start green led
            # sleep(sleeptime)                 # wait 0.5 seconds
 
            # red.stop()
            # green.start(i*2) # greendc start green led
            # sleep(sleeptime)                 # wait 0.5 seconds
 
            
            # green.stop() 
            # blue.start(i*1.5)  # bluedc start blue led
            # sleep(sleeptime)   
            #               # wait 0.5 seconds

            
            # red.start(i*0.2) # reddc  start red led
            # blue.start(1.5*i)  # bluedc start blue led
            # green.start(0.2)
            # sleep(sleeptime)                 # wait 0.5 seconds
 

            # green.stop()
            # red.start(1*i) # reddc  start red led
            # blue.start(1*i)  # bluedc start blue led
            # sleep(sleeptime)
            
            
            # red.stop()                 #stop red led
            # #sleep(sleeptime)                 # wait 0.5 seconds
            # green.stop()               #stop green led
            # #sleep(sleeptime)                 # wait 0.5 seconds
            # blue.stop()                #stop blue led
            # sleep(sleeptime)                 # wait 0.5 seconds
except KeyboardInterrupt:
        red.stop()   #stop red led
        green.stop() #stop green led
        blue.stop()  #stop blue led
        GPIO.cleanup()          # clean up GPIO on CTRL+C exit 	
        print("應用程式結束")