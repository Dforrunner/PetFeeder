import time
from flask import Blueprint, render_template, jsonify, request
from sqlalchemy import asc
from app.modals import Schedule
from . import db
# from rpi_controllers.run_motor import run_motor
# from crontab import CronTab

main = Blueprint('main', __name__)


@main.route('/')
def index():
    schedule = Schedule.query.order_by(asc(Schedule.time)).all()
    return render_template('index.html', schedule=schedule)


@main.route('/feed-now', methods=['POST'])
def feed_now():
    # run_motor(food_amount=5)  # This is actually the number of seconds the motor will be running
    print('feeding')
    time.sleep(5)
    print('fed')
    return jsonify({'success': True})


@main.route('/add-to-schedule', methods=['POST'])
def add_to_schedule():
    add_time = request.form.get('add_time')

    if not unique_time(add_time):
        return jsonify({'success': False})

    if int(add_time) < 24:
        new_time = Schedule(time=int(add_time))
        new_time.save(new_time)

    return jsonify({'success': True, 'time': add_time})


@main.route('/remove-time', methods=['POST'])
def remove_time():
    try:
        rem_time = request.form.get('rem_time')
        sched_time = Schedule.query.filter_by(time=rem_time).first()
        sched_time.delete(sched_time)
    except:
        return jsonify({'success': False})

    return jsonify({'success': True})


# Check if time is unique if not return false
def unique_time(t):
    schedule = Schedule.query.filter_by(time=t).first()
    if schedule is not None:
        return False
    return True
