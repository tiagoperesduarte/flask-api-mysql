from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    done = db.Column(db.Boolean)

    def __init__(self, description, done):
        self.description = description
        self.done = done

    @classmethod
    def from_dict(cls, data):
        return Task(data['description'], data['done'])

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done
        }
