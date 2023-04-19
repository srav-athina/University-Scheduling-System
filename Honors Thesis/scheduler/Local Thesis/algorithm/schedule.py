from data import Data
from course_info.c import Class
import random as rnd

data = Data()


class Schedule:
    def __init__(self):
        self.data = data
        self.classes = []

    def create(self):
        dept = self.data.get_depts()[0]
        courses = dept.get_courses()
        for course in courses:
            new_class = Class(dept, course)
            new_class.set_room(
                data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])

            # set instructor from list of possible instructors in courses
            new_class.set_instructor(course.get_instructors(
            )[rnd.randrange(0, len(course.get_instructors()))])

            # set time based on instructor
            times = new_class.get_instructor().get_ha()

            t = times[rnd.randrange(0, len(times))]
            new_class.set_time(t)

            self.classes.append(new_class)
        return self

    def get_classes(self):
        return self.classes

    def add_class(self, c):
        self.classes.append(c)

    def genConflicts(self):
        prof_conflicts = 0
        dependency_conflicts = 0
        room_conflicts = 0
        course_pref_conflicts = 0
        # professor preferences (they're teaching a class they want to)
        for i in range(len(self.classes)):
            if self.classes[i].get_course().get_number() not in self.classes[i].get_instructor().get_course_prefs():
                course_pref_conflicts += 5
            for j in range(i+1, len(self.classes)):
                # if a class is a dependency of another and they're at the same time, add to conflicts
                if self.classes[i].get_course().is_dependency(self.classes[j].get_course()) and self.classes[i].get_time().check_overlap(self.classes[j].get_time()):
                    dependency_conflicts += 5
                # checks if there's a room clash
                if (self.classes[i].get_room() == self.classes[j].get_room()) and (self.classes[i].get_time().check_overlap(self.classes[j].get_time())):
                    room_conflicts += 2

        prof_times = {}
        # ensure a prof is not double booked
        for c in self.classes:
            if c.get_instructor() in prof_times:
                prof_times[c.get_instructor()].append(c.get_time())
            else:
                prof_times[c.get_instructor()] = [c.get_time()]

        for value in prof_times.values():
            for i in range(len(value)):
                for j in range(i+1, len(value)):
                    if value[i].check_overlap(value[j]):
                        prof_conflicts += 5

        prof_times = {}
        return room_conflicts, prof_conflicts, dependency_conflicts, course_pref_conflicts

    # make penalty more if hard conflict
    def hard_softConflicts(self):
        soft_conflicts = 0
        for i in range(len(self.classes)):
            hard_prefs = self.classes[i].get_instructor().get_ha()
            soft_prefs = self.classes[i].get_instructor().get_sa()

            #if self.classes[i].get_time() not in hard_prefs:
            #    hard_soft_conflicts += 100
            if self.classes[i].get_time() not in soft_prefs:
                 soft_conflicts += 1
        return soft_conflicts
    
    def check_validity(self):
        if sum(self.genConflicts()) != 0:
            return False
        
        for c in self.classes:
            hard_prefs = c.get_instructor().get_ha()
            if c.get_time() not in hard_prefs:
                return False

        return True

    def get_fitness(self, debug=False):
        room_conflicts, prof_conflicts, dependency_conflicts, course_pref_conflicts = self.genConflicts()
        hard_soft_conflicts = self.hard_softConflicts()
        conflicts = prof_conflicts + room_conflicts + dependency_conflicts + course_pref_conflicts + hard_soft_conflicts
        return 1/(conflicts + 1)

    def __str__(self):
        s = ""
        for c in self.classes:
            s += str(c) + "\n"
        return s
