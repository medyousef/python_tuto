import RPi.GPIO as GPIO
import time
LED_LIST=[17,27,16]
BUTTON_PIN=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
for led in LED_LIST:
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
def power_on_selected_led(selected_led):
    if selected_led not in LED_LIST:
        print("The LED does no exsit")
        return
    for led in LED_LIST:
        if led== selected_led:
            GPIO.output(led, GPIO.HIGH)
            print("led on: ", led)
        else:
            GPIO.output(led, GPIO.LOW)
            print("led off: ", led)



previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0
while True:
    time.sleep(0.01)
    current_button_state=GPIO.input(BUTTON_PIN)
    if previous_button_state != current_button_state:
        previous_button_state=current_button_state
        if current_button_state==GPIO.HIGH:
            power_on_selected_led(LED_LIST[led_index])
            led_index +=1
            if led_index >= len(LED_LIST):
                led_index =0

GPIO.cleanup()
