import os
from crontab import CronTab

cron = CronTab(user='pi')


# Path of the script that runs the motor
def run_motor_command():
    basedir = os.path.abspath(os.path.dirname(__file__))
    run_motor_path = os.path.join(basedir, 'rpi_controllers/run_motor.py')
    path = "python3" + run_motor_path
    return path


# Adding cron job
def cron_add(time):
    job = cron.new(command=run_motor_command(), comment=str(time))
    job.day.on(time)
    cron.write()
    return None


# Removing cron job
def cron_remove(time):
    job = cron.find_comment(str(time))
    cron.remove(job)
    cron.write()
    return None


# The functions below are meant for testing alone
def cron_test():
    job = cron.new(command=run_motor_command(), comment='Test')
    job.minute.every(1)
    cron.write()
    return None


def cron_test_done():
    job = cron.find_comment('Test')
    cron.remove(job)
    cron.write()
    return None
