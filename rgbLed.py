from time import sleep 
import RPi.GPIO as GPIO   
GPIO.setmode(GPIO.BCM)

class RGBLed():
    def __init__(self, red_pin, green_pin, blue_pin):
        GPIO.setup(red_pin, GPIO.OUT)# set GPIO 17 as output for blue led  
        GPIO.setup(green_pin, GPIO.OUT)# set GPIO 27 as output for green led  
        GPIO.setup(blue_pin, GPIO.OUT)# set GPIO 22 as output for red led

        self.red = GPIO.PWM(red_pin, 75)
        self.green = GPIO.PWM(green_pin, 75)
        self.blue = GPIO.PWM(blue_pin, 75)
        
        
    def redLight(self):
        try:
            while(True):
                self.red.start(75)
            
        except KeyboardInterrupt:
            self.off()            


    def off(self):
        self.red.stop()   #stop red led
        self.green.stop() #stop green led
        self.blue.stop()  #stop blue led
        GPIO.cleanup()       

    def setColor1(self,*args,second=0.5,forever=False):
        if forever:
            try:
                while (True):
                    for arg in args:    
                        for arga in arg:                        
                            self.red.start((arga[0]/255)*75)
                            self.green.start((arga[1]/255)*75)
                            self.blue.start((arga[2]/255)*75)
                            sleep(second)
                    self.red.start(0)
                    self.green.start(0)
                    self.blue.start(0)
                    sleep(0.5)

            except KeyboardInterrupt:
                self.off() 
        else:
            for arg in args:    
                for arga in arg:                        
                    self.red.start((arga[0]/255)*75)
                    self.green.start((arga[1]/255)*75)
                    self.blue.start((arga[2]/255)*75)
                    sleep(second)

    # 設定顏色 set color
    def setColor(self,r,g,b,second=0.5,forever=False):
        if forever:
            try:
                while (True):
                    self.red.start((r/255)*75)
                    self.green.start((g/255)*75)
                    self.blue.start((b/255)*75)                    
            except KeyboardInterrupt:
                self.off() 
        else:
            self.red.start((r/255)*75)
            self.green.start((g/255)*75)
            self.blue.start((b/255)*75)
            sleep(second)