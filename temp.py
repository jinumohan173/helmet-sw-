#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_Temp = 18
GPIO_pressure = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_Temp, GPIO.OUT)
GPIO.setup(GPIO_pressure, GPIO.OUT)
 

 
if __name__ == '__main__':
    try:
        while True:
            print("loop")            
            sw1 = GPIO.input(GPIO_Temp)
            sw2 = GPIO.input(GPIO_pressure)
            if(sw1==1):
                print("high temp found alert")
            if(sw2==1):
                print("high pressure found alert ")
            time.sleep(1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
