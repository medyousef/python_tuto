import RPi.GPIO as GPIO
import time
BUTTON_PIN=26
LED_PIN_1 = 17
LED_PIN_2 = 27
state=-1
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
while(1):
    if (GPIO.input(BUTTON_PIN)):
        state+=1
        if state==3:
            state=0
        print(state)
        time.sleep(1)


""" previous_button_state=GPIO.input(BUTTON_PIN)
led_index=0
while(1):
    time.sleep(0.01)
    button_state=GPIO.input(BUTTON_PIN)
    if button_state !=previous_button_state:
        previous_button_state=button_state
        if button_state == GPIO.HIGH:
            if led_index==0:
                print(led_index)
                led_index=1
            elif led_index==1:
                print(led_index)
                led_index=2        
            else:
                print(led_index)
                led_index=0 """
                







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

