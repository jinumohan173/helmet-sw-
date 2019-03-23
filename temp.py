#author : Jinu Mohan
#DOC    : 23/03/2019
#Toc    : 1:20 pm

#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_Temp = 21
GPIO_pressure = 20
temp_out = 26
pressure_out = 19

 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_Temp, GPIO.IN)
GPIO.setup(GPIO_pressure, GPIO.IN)

GPIO.setup(temp_out, GPIO.OUT)
GPIO.setup(pressure_out, GPIO.OUT)
 
if __name__ == '__main__':
    try:
        while True:
            print("loop")            
            sw1 = GPIO.input(GPIO_Temp)
            sw2 = GPIO.input(GPIO_pressure)
            if(sw1==1):
                print("high temp found alert")
                GPIO.output(temp_out, 1)
            if(sw2==1):
                print("high pressure found alert ")
                GPIO.output(pressure_out, 1)
            time.sleep(1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
