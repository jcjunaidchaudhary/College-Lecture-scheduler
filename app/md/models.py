from enum import unique
from app import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    username = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    _password = db.Column(db.String(150))
    room = db.relationship('Room')
    lab = db.relationship('Lab')
    instructor = db.relationship('Instructor')
    time = db.relationship('Time')
    Subject = db.relationship('Subject')
    # chapter = db.relationship('Chapter')


    @property
    def password(self):
        """Reading the plaintext password value is not possible or allowed."""
        raise AttributeError("cannot read password")
    
    @password.setter
    def password(self, password):
        """
        Intercept writes to the `password` attribute and hash the given
        password value.
        """
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        """
        Accept a password and hash the value while comparing the hashed
        value to the password hash contained in the database.
        """
        return check_password_hash(self._password, password)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number=db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"<Room:{self.room_number}>"



class Lab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lab=db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"<Lab:{self.lab}>"




class Sem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"<Sem:{self.name}>"

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start=db.Column(db.Integer)
    end=db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"<Time:{self.id}>"

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code=db.Column(db.String(10),unique=True)
    name=db.Column(db.String(12))
    # chapter = db.relationship('Chapter', backref='subject')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    instructor=db.relationship('Instructor',backref='subject',uselist=False)

    def __repr__(self) -> str:
        return f"<Sub:{self.sub_name}>"
    
class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid= db.Column(db.String(12))
    name= db.Column(db.String(12))
    teaching_hour=db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subject_code=db.Column(db.String, db.ForeignKey('subject.code'))

    def __repr__(self) -> str:
        return f"<Instructor:{self.name}>"


# class Chapter(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     number=db.Column(db.Integer)
#     name=db.Column(db.String(12))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     subject_code=db.Column(db.String, db.ForeignKey('subject.code'))

#     def __repr__(self) -> str:
#         return f"<Chap:{self.chap_name}>"
