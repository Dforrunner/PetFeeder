import time
from flask import Blueprint, render_template, jsonify, request
from sqlalchemy import asc
from app.modals import Schedule
# from rpi_controllers.run_motor import run_motor
# from crontab import CronTab

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    schedule = Schedule.query.order_by(asc(Schedule.time))
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
    print(add_time)
    new_time = Schedule(time=add_time)
    new_time.save(new_time)

    return jsonify({'success': True, 'times': add_time})



