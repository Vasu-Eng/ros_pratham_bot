
import RPi.GPIO as GPIO
from  time  import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#definations  and setup
LED = 27  # 18 pwm
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED,GPIO.LOW)




def FADE():
    pwm = GPIO.PWM(LED,1000) #1000 hz
    pwm.start(0)
    for duty in range(0,101,1):
        pwm.ChangeDutyCycle(duty)
        print(f"current duty cycle :{duty}")
        sleep(0.01)
    # pwm.stop()
    for duty in range(99,0,-1):
        pwm.ChangeDutyCycle(duty)
        print(f"current duty cycle :{duty}")
        sleep(0.01)
  
    
def ON():
    GPIO.output(LED,GPIO.HIGH)

def OFF():
    GPIO.output(LED,GPIO.LOW)
 
def blink():
    GPIO.output(LED,GPIO.HIGH)
    sleep(1)
    GPIO.output(LED,GPIO.LOW)
    sleep(1)

# while True:
#      FADE()
    