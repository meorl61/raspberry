import gpiozero as zero
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime


#連線遠端
import requests 

if __name__ == "__main__":
    mcp3008_ch7 = zero.MCP3008(channel = 7)
    mcp3008_ch6 = zero.MCP3008(channel = 6)
    
    try:
        while True:
            value_ch7 = round(mcp3008_ch7.value*100)
            value_ch6 = round(mcp3008_ch6.value*100*3.3*2,2)
            
            if value_ch7 > 11:
                print("光線亮")
            else:
                print("光線暗")
            
            datetimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("光敏電阻値: ", value_ch7)
            print("LM35",value_ch6)

            #git workspace
            #response=requests.get(f'https://meorl61-zany-enigma-6576x9469vjfr5j6-8000.preview.app.github.dev/raspberry?time={datetimeStr}&light={value_ch7}&temperature={value_ch6}')

            #render 免費伺服器
            response=requests.get(f'https://fastapi-3a5p.onrender.com/raspberry?time={datetimeStr}&light={value_ch7}&temperature={value_ch6}')
            if response.ok:
                print("上傳成功")
                print(response.text)
            else:
                print(response.status_code)
            sleep(5)

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程式緊急停止")
