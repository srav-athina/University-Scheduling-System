import random as rnd
import sys
print(sys.path)
sys.path.append("C:\\Users\\jnaat\\OneDrive\\Documents\\School\\Thesis\\Honors Thesis\\scheduler\\LocalThesis")

from course_info.c import Class
from course_info.instructor import Instructor
from course_info.course import Course
from course_info.room import Room
from course_info.meeting_time import ClassTime
DEPT = "CSE"

class Schedule:
    def __init__(self, course_inputs, dependencies, profs_inputs, hard_prefs_inputs, soft_prefs_inputs, course_prefs_inputs, rooms_inputs):
        self.classes = []

        # make courses, instructors, times, & rooms
        rooms = []
        for room in rooms_inputs:
            rooms.append(Room(room[0], room[1]))

        hard_times = []
        soft_times = []
        for i in range(len(hard_prefs_inputs)):
            curr = []
            for j in range(len(hard_prefs_inputs[i])):
                ht = ClassTime(hard_prefs_inputs[i][j][0], hard_prefs_inputs[i][j][1], hard_prefs_inputs[i][j][2])
                curr.append(ht)
            hard_times.append(curr)
        for i in range(len(soft_prefs_inputs)):
            curr = []
            for j in range(len(soft_prefs_inputs[i])):
                st = ClassTime(soft_prefs_inputs[i][j][0], soft_prefs_inputs[i][j][1], soft_prefs_inputs[i][j][2])
                curr.append(st)
            soft_times.append(curr)

        # course_prefs_inputs should be a list of lists of strings (w/ just course number)
        instructors = []
        for i in range(len(profs_inputs)):
            prof = Instructor(
                profs_inputs[i], hard_times[i], soft_times[i], course_prefs_inputs[i])
            instructors.append(prof)

        courses = []
        # should just be name and stuff
        for key, value in course_inputs.items():
            new_course = Course(value[0]+key, value[1], instructors, value[2])
            courses.append(new_course)

        #print(dependencies)
        for c1 in courses:
            for c2 in courses:
                if c1.get_number() in dependencies and c2.get_number() in dependencies[c1.get_number()]:
                    c1.add_dependencies(c2)

        for course in courses:
            new_class = Class(DEPT, course)
            new_class.set_room(rooms[rnd.randrange(0, len(rooms))])

            # set instructor from list of possible instructors in courses
            new_class.set_instructor(
                instructors[rnd.randrange(0, len(instructors))])

            # set time based on instructor
            times = new_class.get_instructor().get_ha()
            #print(times)

            t = times[rnd.randrange(0, len(times))]
            new_class.set_time(t)

            self.classes.append(new_class)

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

            # if self.classes[i].get_time() not in hard_prefs:
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
        conflicts = prof_conflicts + room_conflicts + \
            dependency_conflicts + course_pref_conflicts + hard_soft_conflicts
        return 1/(conflicts + 1)

    def __str__(self):
        s = ""
        for c in self.classes:
            s += str(c) + "\n"
        return s
