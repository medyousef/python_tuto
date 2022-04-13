import RPi.GPIO as GPIO
import time
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
state=int(input("1 to start 0 to exit"))
if state==1:
    while(1):
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN,GPIO.LOW)
elif state==0:
    exit
else:
    print("wrong number")
GPIO.cleanup()
