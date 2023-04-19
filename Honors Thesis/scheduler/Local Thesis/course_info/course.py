from course_info.instructor import Instructor

class Course():
    def __init__(self, number, name, instructors, credit_hours):
        self.number = number #string
        self.name = name #string
        self.instructors = instructors #list of instructors
        self.credit_hours = credit_hours
        self.dependencies = [] #list of courses
        #we probably need a variable for number of instructors if we're doing multiple
    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_instructors(self):
        return self.instructors

    def get_dependencies(self):
        return self.dependencies

    def is_dependency(self, other):
        #check to see if our course is in the list of the other course's dependencies
        for d in other.get_dependencies():
            if d == self:
                return True
        return False

    #d is a list
    def add_dependencies(self, d):
        for c in d:
            self.dependencies.append(c)

    def get_credit_hours(self):
        return self.credit_hours

    def __str__(self):
        return self.name

