import RPi.GPIO as GPIO
import time


def set_motor_time(t):
    fin = open("motor_runtime.txt", "r")
    fout = open("motor_runtime.txt", "w")
    first_row = True
    for row in fin:
        if first_row:
            row = str(t)
            first_row = False
        fout.write(row)
    f.close()


def get_motor_runtime():
    f = open("motor_runtime.txt", "r")
    line = f.read().splitlines(True)
    return int(line[0])


def run_unclug_motor(run_time):
    pin = 15
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, GPIO.LOW)
    time.sleep(run_time)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(run_time)
    GPIO.output(pin, GPIO.HIGH)

def run_motor(food_amount):
    pin = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)

    run_unclug_motor(0.5)

# I'm using a Sainsmart 4 relay module which works backwards mean LOW turns it on and HIGH turns it off.
    GPIO.output(pin, GPIO.LOW) # converoy belt
    print('feeding...')
    time.sleep(food_amount)
    GPIO.output(pin, GPIO.HIGH)
    print('complete!')

    run_unclug_motor(0.5)

    GPIO.cleanup()
    return None


if __name__ == '__main__':
    run_motor(3)

