from flask_restful import Api
from flask import Blueprint
from app.md.controllers.views import  DetailsView, FacultyView, LabView, RoomView, SemView, CourseView, TimeView,TimeTable



md_blueprint =Blueprint("md",__name__,url_prefix="/md")
api=Api(md_blueprint)

# http://127.0.0.1:5000/api/md/note
api.add_resource(DetailsView,"/details/")
api.add_resource(RoomView,"/room/") 
api.add_resource(LabView,"/lab/") 
api.add_resource(FacultyView,"/faculty/") 
api.add_resource(SemView,"/sem/") 
api.add_resource(TimeView,"/time/") 
api.add_resource(CourseView,"/course/") 
api.add_resource(TimeTable,"/timetable/") 
# api.add_resource(ChapterView,"/chapter/") 

