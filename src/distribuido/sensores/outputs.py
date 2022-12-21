import RPi.GPIO as GPIO
import time

def outputs(pino):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pino, GPIO.OUT)

    if(GPIO.input(pino)):
        GPIO.output(pino, GPIO.LOW)
        return 'OFF'
    else:
        GPIO.output(pino, GPIO.HIGH)
        return 'ON'