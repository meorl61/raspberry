#!/usr/bin/python3

from rgbLed import RGBLed
from time import sleep 

if __name__ == "__main__":
    rgb = RGBLed(22,27,17)
    #rgb.redLight()

    #args = [[255,153,0],[242,133,0],[255,140,0],[255,127,80]]
    args = [[255,0,0],[255,153,0],[255,255,0],[0,255,0],[0,0,255],[0,77,153],[160,32,240]]
    rgb.setColor1(args,second=0.8,forever=True)
    sleep(1)
    rgb.off()
    


