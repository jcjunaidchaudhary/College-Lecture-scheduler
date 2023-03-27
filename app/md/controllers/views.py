from flask import jsonify, request, session
from flask_restful import Resource
from app import db
from app.md.models import Faculty, Lab, Room, Sem, Course, Time, User
from app.md.serde import  FacultySchema, LabSchema, RoomSchema, SemSchema, CourseSchema, TimeSchema, UserSchema
import random 
import numpy as np


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
        
        Course=Course.query.filter_by(id=session['user_id']).all()
        CourseSchema=CourseSchema().dump(Course,many=True)
        
        Faculty=Faculty.query.filter_by(id=session['user_id']).all()
        FacultySchema=FacultySchema().dump(Faculty,many=True)
        
        return jsonify({"user":userSchema,"rooms":roomSchema,"labs":labSchema,"sem":semSchema,"time":timeSchema,"Courses":CourseSchema,"Facultys":FacultySchema})


class TimeTable(Resource):
    def post(self):
        data=request.get_json()
        lst = []
        d = 0
        p = 0
        subnum = Course.query.filter_by(sem_id=data["sem_id"]).count()
        sub=Course.query.filter(Course.sem_id==data["sem_id"]).all()
        print(subnum)
        print(sub[0].faculty.uid)
        # print(CourseSchema(many=True).dump(sub))
        return "hello"

        for i in range(0, subnum):
            sub = input("enter subject :")
            f = int(input("enter frequency :"))
            d = d + f
            for i in range(0, f):
                lst.append(sub)
        if (d > 35):
            print("invalid input")
        else:
            for i in range(0, 35 - d):
                ele = "   "
                lst.append(ele)
        R = 7
        C = 5
        k = int(input("enter number of timetables"))
        for p in range(k):
            lst1 = []
            matrix = []
            m = []
            time = ["9-10  ", "10-11 ", "11-12 ", "12-1  ", "2-3   ","3-4  ","4-5  "]
            for i in range(R):
                a = []
                for j in range(C):
                    item = lst[0]
                    a.append(item)
                    lst.remove(item)
                    lst1.append(item)
                matrix.append(a)
                m = np.array(matrix)
                matrix1 = m.T
                for e in range(5):
                    random.shuffle(matrix1[e])
                m1 = np.array(matrix1)
                matrix2 = m1.T
            for m in range(30):
                lst.append(lst1[m])
            print("-----FE ", end="")
            print(p + 1, end="")
            print("------")
            print("TIME  MON  TUE  WED  THU  FRI")
            for i in range(R):
                print(time[i], end="")
                for j in range(C):
                    print(matrix2[i][j], end="  ")
                print()
        
class SemView(Resource):
    
    def get(self):
        sem=Sem.query.all()
        return SemSchema(many=True).dump(sem)
    
    def post(self):
        data = request.get_json()
        sem = Sem(**data)
        db.session.add(sem)
        db.session.commit()
        return SemSchema().dump(sem)
    

class CourseView(Resource):
    def get(self):
        sub=Course.query.all()
        return CourseSchema(many=True).dump(sub)

    def post(self):
        data = request.get_json()
        sub = Course(**data)
        db.session.add(sub)
        db.session.commit()
        return CourseSchema().dump(sub)
    

class FacultyView(Resource):
    
    def get(self):
        faculty=Faculty.query.all()
        return FacultySchema(many=True).dump(faculty)
    
    def post(self):
        data = request.get_json()
        faculty = Faculty(**data)
        db.session.add(faculty)
        db.session.commit()
        return FacultySchema().dump(faculty)

class RoomView(Resource):
    
    def get(self):
        room=Room.query.all()
        return RoomSchema(many=True).dump(room)
    
    def post(self):
        data = request.get_json()
        room = Room(**data)
        db.session.add(room)
        db.session.commit()
        return RoomSchema().dump(room)
    
    def delete(self):
        data=request.get_json()
        Room.query.filter(Room.id.in_([f["id"] for f in data])).delete()
        db.session.commit()
        return ""


class LabView(Resource):
    
    def get(self):
        lab=Lab.query.all()
        return LabSchema(many=True).dump(lab)
    
    def post(self):
        data = request.get_json()
        lab = Lab(lab=data['lab'], user_id=session['user_id'])
        db.session.add(lab)
        db.session.commit()
        return LabSchema().dump(lab)



class TimeView(Resource):

    def get(self):
        time=Time.query.all()
        return TimeSchema().dump(time)
    
    def post(self):
        data = request.get_json()
        time = Time(**data, user_id=session['user_id'])
        db.session.add(time)
        db.session.commit()
        return TimeSchema().dump(time)




# class ChapterView(Resource):
#     def get(self):
#         return{'Chapter':'success'}
#     def post(self):
#         data = request.get_json()
#         chap = Chapter(**data, user_id=session['user_id'])
#         db.session.add(chap)
#         db.session.commit()
#         return ChapterSchema().dump(chap)
    