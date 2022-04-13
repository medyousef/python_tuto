import RPi.GPIO as GPIO
import time
BUTTON_PIN=26
LED_PIN_1 = 17
LED_PIN_2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

previous_button_state=GPIO.input(BUTTON_PIN)
led_index=0
while(1):
    time.sleep(0.01)
    button_state=GPIO.input(BUTTON_PIN)
    if button_state !=previous_button_state:
        previous_button_state=button_state
        if button_state == GPIO.HIGH:
            if led_index==0:
                GPIO.output(LED_PIN_1,GPIO.HIGH)
                GPIO.output(LED_PIN_2,GPIO.LOW)
                led_index=1
                print(led_index)
            elif led_index==1:
                GPIO.output(LED_PIN_1,GPIO.LOW)
                GPIO.output(LED_PIN_2,GPIO.HIGH)
                led_index=2 
                print(led_index)       
            else:
                GPIO.output(LED_PIN_1,GPIO.HIGH)
                GPIO.output(LED_PIN_2,GPIO.HIGH)
                print(led_index)
                led_index=0
                







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

