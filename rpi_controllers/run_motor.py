import RPi.GPIO as GPIO
import time


def run_motor():
    pin = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, GPIO.HIGH)
    print('feeding...')
    time.sleep(5)
    GPIO.output(pin, GPIO.LOW)
    print('complete!')
    GPIO.cleanup()
    return None

