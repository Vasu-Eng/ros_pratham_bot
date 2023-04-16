import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#defination 
Buttonpin = 17
#pin mode
GPIO.setup(Buttonpin, GPIO.IN ,pull_up_down=GPIO.PUD_UP)

def button_status():
    button_status = GPIO.input(Buttonpin)
    if button_status == GPIO.HIGH:
        print("button was pressed !!")
        return "on"
    elif button_status == GPIO.LOW:
        return "off"
    return "invalid !!"

# while True :
#   val = GPIO.input(Buttonpin)
# #   print(val)