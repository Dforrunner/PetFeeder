import os
from flask import Flask, render_template
from forms import IntervalForm
from rpi_controllers.run_motor import run_motor
from crontab import CronTab
# from run_motor import run_motor
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ebehlb34lti43ubfui3n4589hfi4fkejhbkuydwlsbaye'

interval = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    form = IntervalForm()
    # feed(form.interval.data)

    return render_template('index.html', form=form)


@app.route('/feed-now', methods=['POST'])
def feed_now():
    run_motor()
    return 'feedings...'


# cron = CronTab(user='pi')
# job = cron.new(command='python3 example1.py')
# job.hour.every(interval)
#
# cron.write()

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=feed, trigger="interval", seconds=3)
# scheduler.start()

if __name__ == '__main__':
    # scheduler = BlockingScheduler()
    # scheduler.add_executor('app')
    # scheduler.add_job(feed, 'interval', seconds=interval)
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    #
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass
    app.run(host='0.0.0.0', debug=True)
