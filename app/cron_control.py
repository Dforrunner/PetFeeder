import os
from crontab import CronTab

cron = CronTab(user='pi')


# Path of the script that runs the motor
def run_motor_command():
    basedir = os.path.abspath(os.path.dirname(__file__))
    run_motor_path = os.path.join(basedir, 'rpi_controllers/run_motor.py')
    return f"python3 {run_motor_path}"


# Adding cron job
def cron_add(time):
    job = cron.new(command=run_motor_command(), comment=f'{time}')
    job.day.on(time)
    cron.write()
    return None


# Removing cron job
def cron_remove(time):
    job = cron.find_comment(f'{time}')
    cron.remove(job)
    cron.write()
    return None
