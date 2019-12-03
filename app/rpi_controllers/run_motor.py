import RPi.GPIO as GPIO
import time
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def set_motor_runtime(t):
    f = open(os.path.join(__location__, 'motor_runtime.txt'), "r+")
    f.truncate()
    f.write(str(t))
    f.close()


def get_motor_runtime():
    f = open(os.path.join(__location__, 'motor_runtime.txt'), "r")
    line = f.read().splitlines(True)
    return float(line[0])


def run_unclog_motor():
    pin = 15
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)


def run_motor(food_amount):
    pin = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    loop_num = 1

    # The dispenser hole gets clogged again after the unclog motor is done running.
    # Meaning if we were to run the conveyor that dispenses the food into the bowl for more than 2-3 seconds we won't
    # be getting any food. So we need to remember to run the unclog motor in short intervals
    if 3 < food_amount < 6:
        loop_num = 2
        food_amount = round(food_amount/2, 1)
    elif food_amount > 6:
        loop_num = 3
        food_amount = round(food_amount/3, 1)

    for i in range(1, loop_num):
        run_unclog_motor()

        # I'm using a Sainsmart 4 relay module which works backwards mean LOW turns it on and HIGH turns it off.
        GPIO.output(pin, GPIO.LOW) # converoy belt
        print('feeding...')
        time.sleep(food_amount())
        GPIO.output(pin, GPIO.HIGH)
        print('complete!')

    run_unclog_motor()
    GPIO.cleanup()
    return None


if __name__ == '__main__':
    run_motor(get_motor_runtime())

