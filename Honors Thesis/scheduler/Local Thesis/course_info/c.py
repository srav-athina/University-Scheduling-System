from course_info.instructor import Instructor
from course_info.course import Course
from course_info.dept import Dept

class Class:
    def __init__(self, dept, course):
        self.dept = dept
        self.course = course
        self.instructor = None
        self.time = None
        self.room = None
        self.TAs = None

    def get_id(self):
        return self.ID

    def get_dept(self):
        return self.dept

    def get_course(self):
        return self.course

    def get_instructor(self):
        return self.instructor
    
    def get_TAs(self):
        return self.TAs

    #an object
    def get_time(self):
        return self.time

    def get_room(self):
        return self.room

    def set_instructor(self, i):
        if i.get_type() == "TA":
            self.TAs.append(i)
        else:
            self.instructor = i

    def add_TA(self, t):
        self.TAs.append(t)

    def set_time(self, time):
        self.time = time

    def set_room(self, room):
        self.room = room

    def __str__(self):
        return str(self.get_dept()) + str(self.get_course().get_number()) + ", " + str(self.get_course().get_name()) + ", " + str(self.get_instructor().get_name()) + ", " + str(self.get_time()) + ", " + str(self.get_room())

