import RPi.GPIO as GPIO
import time
BUTTON_PIN=26
LED_PIN_1 = 17
LED_PIN_2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
i=-1
while(1):
    if (GPIO.input(BUTTON_PIN)):
        i+=1
        if i==3:
            i=0
        print(i)
        time.sleep(1)



GPIO.cleanup()

""" if state==1:
    while(1):
        GPIO.output(LED_PIN,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN,GPIO.LOW)
        time.sleep(1)
elif state==0:
    GPIO.output(LED_PIN,GPIO.LOW)
else:
    print("wrong number")
    GPIO.cleanup()
    exit """

