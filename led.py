import RPi.GPIO as GPIO
import time
BUTTON_PIN=26
LED_PIN_1 = 17
LED_PIN_2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)
while(1):
    if (GPIO.input(BUTTON_PIN)):
        GPIO.output(LED_PIN_1,GPIO.HIGH)
        GPIO.output(LED_PIN_2,GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED_PIN_1,GPIO.LOW)
        GPIO.output(LED_PIN_2,GPIO.HIGH)
        time.sleep(1)
        print("button pressed, LEDs blinks")
    else:
        GPIO.output(LED_PIN_1,GPIO.LOW)
        PIO.output(LED_PIN_2,GPIO.LOW)
        print("button released, LEDs Off")
        time.sleep(2)

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

