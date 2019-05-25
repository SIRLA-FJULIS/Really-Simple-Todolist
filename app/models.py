from . import db

class TaskDate(db.Model):
    __tablename__ = 'taskdate'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)

    def __repr__(self):
        return '<TaskDate %r>' % self.date

class TaskItem(db.Model):
    __tablename__ = 'taskitem'
    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(64), unique = True, index = True)

    def __repr__(self):
        return '<TaskItem %r>' % self.item