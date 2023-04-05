# pages/urls.py
from django.urls import path
from pages.views import *

urlpatterns = [
    path("professor_options/", profOptionsView, name="profOptions"),
    path("add_professor/", addProfessorView, name="addProfessor"),
    path("add_professor_conf/", addProfessorConfView, name="addProfessorConf"),
    path("update_prof/", updateProfView, name="updateProf"),
    path("update_prof_conf/", updateProfConfView, name="updateProfConf"),


    path("curr_data/", currDataView, name="currData"),

    path("output/", outputPageView, name="output"), 

    path("directory_manager/", directoryView, name="directoryManager"),
    path("add_course/", addCourseView, name="addCourse"),
    path("add_course_conf/", addCourseConfView, name="addCourseConf"),
    path("remove_course/", removeCourseView, name="removeCourse"),
    path("remove_course_conf/", removeCourseConfView, name="removeCourse"),

    path("update_course/", updateCourseView, name="updateCourse"),
    path("update_course_conf/", updateCourseConfView, name="updateCourseConf"),

    path("add_remove_dependency/", addRemoveDependencyView, name="addRemoveDependency"),
    path("remove_dependency/", removeDependencyView, name="removeDependency"),
    path("remove_dependency_conf/", removeDependencyConfView, name="removeDependencyConf"),
    path("add_dependency/", addDependencyView, name="addDependency"),
    path("add_dependency_conf/", addDependencyConfView, name="addDependencyConf"),

    path("", homePageView, name="home"),
]