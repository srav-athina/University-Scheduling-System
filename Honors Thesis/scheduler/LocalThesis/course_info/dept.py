from course_info.course import Course

class Dept:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def get_name(self):
        return self.name
    
    def get_courses(self):
        return self.courses

    def add_course(self, c):
        self.courses.append(c)

    def __str__(self):
        return self.get_name()

