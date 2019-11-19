# import RPi.GPIO as GPIO
# import time
#
#
# def run_motor(food_amount):
#     pin = 14
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(pin, GPIO.OUT)
#
#     # I'm using a Sainsmart 4 relay module which works backwards mean LOW turns it on and HIGH turns it off.
#     GPIO.output(pin, GPIO.LOW)
#     print('feeding...')
#     time.sleep(food_amount)
#     GPIO.output(pin, GPIO.HIGH)
#     print('complete!')
#     GPIO.cleanup()
#     return None

