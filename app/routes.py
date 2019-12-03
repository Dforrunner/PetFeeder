from flask import Blueprint, render_template, jsonify, request
from sqlalchemy import asc
from app.modals import Schedule
from .rpi_controllers.run_motor import set_motor_runtime, get_motor_runtime, run_motor
from .cron_control import cron_add, cron_remove

main = Blueprint('main', __name__)


@main.route('/')
def index():
    schedule = Schedule.query.order_by(asc(Schedule.time)).all()
    return render_template('index.html', schedule=schedule, motor_time_value=get_motor_runtime())


@main.route('/feed-now', methods=['POST'])
def feed_now():
    # Run the motor now
    run_motor(food_amount=get_motor_runtime())  # This is actually the number of seconds the motor will be running
    return jsonify({'success': True})


@main.route('/add-to-schedule', methods=['POST'])
def add_to_schedule():
    # Get time from request
    add_time = request.form.get('add_time')

    # Check if time is unique, because no duplicate time are allowed
    if not unique_time(add_time):
        return jsonify({'success': False})

    if int(add_time) < 24:
        # Add time to database
        new_time = Schedule(time=int(add_time))
        new_time.save(new_time)

        # Add time to cron
        cron_add(add_time)

    return jsonify({'success': True, 'time': add_time})


@main.route('/remove-time', methods=['POST'])
def remove_time():
    try:
        # Get time from request
        rem_time = request.form.get('rem_time')

        # Remove time from database
        sched_time = Schedule.query.filter_by(time=rem_time).first()
        sched_time.delete(sched_time)

        # Remove time from cron
        cron_remove(rem_time)
    except:
        return jsonify({'success': False})

    return jsonify({'success': True})


@main.route('/set-motor-time', methods=['POST'])
def set_motor_time():
    try:
        motor_runtime = request.form.get('motor_runtime')
        # print(motor_runtime)
        set_motor_runtime(motor_runtime)
    except:
        return jsonify({'success': False})

    return jsonify({'success': True})


# Check if time is unique if not return false
def unique_time(t):
    schedule = Schedule.query.filter_by(time=t).first()
    if schedule is not None:
        return False
    return True
