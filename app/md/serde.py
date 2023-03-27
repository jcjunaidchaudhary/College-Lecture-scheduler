from marshmallow import Schema, fields

from app.md.models import Faculty, Lab, Room, Sem, Course, Time


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    username = fields.Str()
    email = fields.Str()
    join_date = fields.Date(dump_only=True)


class RoomSchema(Schema):
    class Meta:
        load_instance = True
        model = Room
        fields = [
            "id",
            "number",
            
        ]

class LabSchema(Schema):
    class Meta:
        load_instance = True
        model = Lab
        fields = [
            "id",
            "lab",
            "sem_id"
            
        ]

class FacultySchema(Schema):
    class Meta:
        load_instance = True
        model = Faculty
        fields = [
            "id",
            "uid",
            "name",
            "teaching_hour",
            "subject_code",
        
        ]

class SemSchema(Schema):
    class Meta:
        load_instance = True
        model = Sem
        fields = [
            "id",
            "name",
            "faculty_count",
            "sub_count"
            
        ]

class TimeSchema(Schema):
    class Meta:
        load_instance = True
        model = Time
        fields = [
            "id",
            "start",
            "end"
        ]
class CourseSchema(Schema):
    class Meta:
        load_instance = True
        model = Course
        fields = [
            "id",
            "code",
            "name",
            "teaching_hour",
            "sem_id",
        ]
# class ChapterSchema(Schema):
#     class Meta:
#         load_instance = True
#         model = Chapter
#         fields = [
#             "id",
#             "number",
#             "name",
#             "subject_code"
#         ]

