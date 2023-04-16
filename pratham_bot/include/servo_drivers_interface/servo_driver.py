from gpiozero import Servo
from time import sleep

servo_pan = Servo(25)
servo_tilt = Servo(24) # pin changed accordingly


def writeServo(pose_pan,pose_tilt):
        print(f"pose_pan : {pose_pan} \n pose_tilt : {pose_tilt}")
        servo_tilt.value = pose_tilt
        servo_pan.value = pose_pan
        sleep(0.01)

        
