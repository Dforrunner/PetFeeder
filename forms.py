from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class IntervalForm(FlaskForm):
    interval = SelectField('Intervals', choices=((0, 'Choose Interval'),
                                                 (2, '2 hr'),
                                                 (4, '4 hr'),
                                                 (6, '6 hr'),
                                                 (8, '8 hr'),
                                                 (10, '10 hr'),
                                                 (12, '13 hr'),
                                                 (14, '14 hr'),
                                                 (16, '16 hr'),
                                                 (18, '18 hr'),
                                                 (20, '20 hr'),
                                                 (22, '22 hr'),
                                                 (24, '24 hr'),))
    submit = SubmitField('Set Interval')


