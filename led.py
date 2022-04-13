import RPi.GPIO as GPIO
import time
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
while(1):
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN,GPIO.LOW)
GPIO.cleanup()
