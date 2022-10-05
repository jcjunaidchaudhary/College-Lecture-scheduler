from marshmallow import Schema, fields

from app.md.models import Instructor, Lab, Room, Sem, Subject, Time


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
            
        ]

class InstructorSchema(Schema):
    class Meta:
        load_instance = True
        model = Instructor
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
class SubjectSchema(Schema):
    class Meta:
        load_instance = True
        model = Subject
        fields = [
            "id",
            "code",
            "name"
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

