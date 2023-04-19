# would actually come from a database
from course_info.instructor import Instructor
from course_info.course import Course
from course_info.room import Room
from course_info.dept import Dept
from data_inputs import hard_prefs, soft_prefs, rooms, instructors, course_prefs

class Data:
    def __init__(self):
        self.instructors = []
        self.rooms = []
        self.courses = []

        for room in rooms:
            self.rooms.append(Room(room[0], room[1]))
        for i in range(len(instructors)):
            self.instructors.append(Instructor(instructors[i], hard_prefs[i], soft_prefs[i], course_prefs[i]))

        c1 = Course('1010', 'Computing', self.instructors, 3)
        c2 = Course('2050', 'Data Structures', self.instructors, 3)
        c3 = Course('2500', 'Discrete Systems', self.instructors, 3)
        c4 = Course('3100', 'Systems Programming', self.instructors, 3)
        c5 = Course('3500', 'Algorithms', self.instructors, 3)
        c6 = Course('3666', 'Comp. Arch', self.instructors, 3)
        c7 = Course('4502', 'Big Data Analytics', self.instructors, 4)
        c8 = Course('2102', 'Software Design', self.instructors, 3)
        c9 = Course('3504', 'Prob. Perf. Analysis', self.instructors, 3)
        
        c2.add_dependencies([c3])
        c3.add_dependencies([c2])
        c4.add_dependencies([c5, c6])
        c5.add_dependencies([c4, c6])
        c6.add_dependencies([c4, c5])

        self.courses = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
        self.depts = [Dept('CSE', self.courses)]
    
    def get_rooms(self):
        return self.rooms

    def get_instructors(self):
        return self.instructors

    def get_courses(self):
        return self.courses

    def get_depts(self):
        return self.depts

    def get_meetingTimes(self):
        return self.mts

Data()