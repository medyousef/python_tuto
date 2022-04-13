import RPi.GPIO as GPIO
import time
BUTTON_PIN=26
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
""" state=int(input("1 to start 0 to exit: ")) """
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)
while(1):
    print(GPIO.input(BUTTON_PIN))
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

