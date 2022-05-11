import RPi.GPIO as GPIO
import time
LED_LIST=[17,27,16]
BUTTON_PIN=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(*LED_LIST,GPIO.OUT)
GPIO.output(*LED_LIST,GPIO.LOW)
previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0
while True:
    time.sleep(0.01)
    current_button_state=GPIO.input(BUTTON_PIN)
    if previous_button_state != current_button_state:
        previous_button_state=current_button_state
        if current_button_state==GPIO.HIGH:
            if led_index==0:
                GPIO.output(LED_LIST[0:1], GPIO.LOW)
                GPIO.output(LED_LIST[2], GPIO.HIGH)
                print ("LED ON: ",LED_LIST[2], "LED OFF:",LED_LIST[0:1] )
                led_index=1
            elif led_index==1:
                GPIO.output(LED_LIST[1:2], GPIO.LOW)
                GPIO.output(LED_LIST[0], GPIO.HIGH)
                led_index=2
                print ("LED ON: ",LED_LIST[0], "LED OFF:",LED_LIST[1:2] )
            else:    
                GPIO.output(LED_LIST[0,2], GPIO.LOW)
                GPIO.output(LED_LIST[1], GPIO.HIGH)
                print ("LED ON: ",LED_LIST[1], "LED OFF:",LED_LIST[0,2] )
                led_index=0

GPIO.cleanup()
