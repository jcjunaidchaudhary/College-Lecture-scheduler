from flask_restful import Api
from flask import Blueprint
from app.md.controllers.views import  DetailsView, InstructorView, LabView, RoomView, SemView, SubjectView, TimeView



md_blueprint =Blueprint("md",__name__,url_prefix="/md")
api=Api(md_blueprint)

# http://127.0.0.1:5000/api/md/note
api.add_resource(DetailsView,"/details/")
api.add_resource(RoomView,"/room/") 
api.add_resource(LabView,"/lab/") 
api.add_resource(InstructorView,"/instructor/") 
api.add_resource(SemView,"/sem/") 
api.add_resource(TimeView,"/time/") 
api.add_resource(SubjectView,"/subject/") 
# api.add_resource(ChapterView,"/chapter/") 

