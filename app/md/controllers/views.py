from flask import jsonify, request, session
from flask_restful import Resource
from app import db
from app.md.models import Instructor, Lab, Room, Sem, Subject, Time, User
from app.md.serde import  InstructorSchema, LabSchema, RoomSchema, SemSchema, SubjectSchema, TimeSchema, UserSchema


class DetailsView(Resource):
    def get(self):
        user=User.query.filter_by(id=session['user_id']).first()
        userSchema=UserSchema().dump(user)
        
        room=Room.query.filter_by(id=session['user_id']).all()
        roomSchema=RoomSchema().dump(room,many=True)
        
        lab=Lab.query.filter_by(id=session['user_id']).all()
        labSchema=LabSchema().dump(lab,many=True)
        
        sem=Sem.query.filter_by(id=session['user_id']).all()
        semSchema=SemSchema().dump(sem,many=True)
        
        time=Time.query.filter_by(id=session['user_id']).first()
        timeSchema=TimeSchema().dump(time)
        
        subject=Subject.query.filter_by(id=session['user_id']).all()
        subjectSchema=SubjectSchema().dump(subject,many=True)
        
        instructor=Instructor.query.filter_by(id=session['user_id']).all()
        instructorSchema=InstructorSchema().dump(instructor,many=True)
        
        return jsonify({"user":userSchema,"rooms":roomSchema,"labs":labSchema,"sem":semSchema,"time":timeSchema,"subjects":subjectSchema,"instructors":instructorSchema})

        


class RoomView(Resource):
    def get(self):
        return{'room':'success'}
    def post(self):
        data = request.get_json()
        room = Room(number=data['number'], user_id=session['user_id'])
        db.session.add(room)
        db.session.commit()
        return RoomSchema().dump(room)

class LabView(Resource):
    def get(self):
        return{'lab':'success'}
    def post(self):
        data = request.get_json()
        lab = Lab(lab=data['lab'], user_id=session['user_id'])
        db.session.add(lab)
        db.session.commit()
        return LabSchema().dump(lab)

class InstructorView(Resource):
    def get(self):
        return{'Instructor':'success'}
    def post(self):
        data = request.get_json()
        instructor = Instructor(**data, user_id=session['user_id'])
        db.session.add(instructor)
        db.session.commit()
        return InstructorSchema().dump(instructor)

class SemView(Resource):
    def get(self):
        return{'Sem':'success'}
    def post(self):
        data = request.get_json()
        sem = Sem(**data, user_id=session['user_id'])
        db.session.add(sem)
        db.session.commit()
        return SemSchema().dump(sem)


class TimeView(Resource):
    def get(self):
        return{'Time':'success'}
    def post(self):
        data = request.get_json()
        time = Time(**data, user_id=session['user_id'])
        db.session.add(time)
        db.session.commit()
        return TimeSchema().dump(time)

class SubjectView(Resource):
    def get(self):
        return{'Subject':'success'}
    def post(self):
        data = request.get_json()
        sub = Subject(**data, user_id=session['user_id'])
        db.session.add(sub)
        db.session.commit()
        return SubjectSchema().dump(sub)

# class ChapterView(Resource):
#     def get(self):
#         return{'Chapter':'success'}
#     def post(self):
#         data = request.get_json()
#         chap = Chapter(**data, user_id=session['user_id'])
#         db.session.add(chap)
#         db.session.commit()
#         return ChapterSchema().dump(chap)
    