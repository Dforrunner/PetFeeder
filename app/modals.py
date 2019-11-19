from . import db


class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    @classmethod
    def get_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
                raise
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


class Schedule(CRUDMixin, db.Model):
    __tablename__ = 'scheduled_times'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, time):
        self.time = time
