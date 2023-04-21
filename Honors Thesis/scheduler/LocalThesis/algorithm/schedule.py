import random as rnd
import sys
sys.path.append("C:\\Users\\jnaat\\OneDrive\\Documents\\School\\Thesis\\Honors Thesis\\scheduler\\LocalThesis")

from course_info.c import Class
from course_info.instructor import Instructor
from course_info.course import Course
from course_info.room import Room
from course_info.meeting_time import ClassTime
DEPT = "CSE"

class Schedule:
    def __init__(self, courses, dependencies, instructors, hard_times, soft_times, course_prefs_inputs, rooms):
        self.classes = []
        self.soft_conflicts = 0
        self.course_pref_conflicts = 0
        self.room_conflicts = 0
        self.dependency_conflicts = 0
        self.prof_conflicts = 0
        self.room_times = {}
        self.class_times = {}
        self.prof_times = {}

        # make courses, instructors, times, & rooms
        # hard_pref_inputs = [[(), (), ()]]

        # course_prefs_inputs should be a list of lists of strings (w/ just course number)

        #print(dependencies)

        for course in courses:
            new_class = Class(DEPT, course)
            chosen_room = rooms[rnd.randrange(0, len(rooms))]
            chosen_prof = course.get_instructors()[rnd.randrange(0, len(course.get_instructors()))]

            new_class.set_room(chosen_room)

            # set instructor from list of possible instructors in courses
            new_class.set_instructor(chosen_prof)

            # set time based on instructor
            hard_times = new_class.get_instructor().get_ha()
            soft_times = new_class.get_instructor().get_sa()
            # Calculate the number of tuples to select from each list
            hard_count = int(len(hard_times) * 0.2)
            soft_count = int(len(soft_times) * 0.8)
            # Randomly select the tuples from each list
            selected_hard_times = rnd.sample(hard_times, hard_count)
            selected_soft_times = rnd.sample(soft_times, soft_count)

            # Combine the selected tuples into a new list
            times = selected_hard_times + selected_soft_times

            t = times[rnd.randrange(0, len(times))]
            new_class.set_time(t)
            self.class_times[new_class.get_course().get_name()] = t
            
            # calculate conflicts

            if t not in chosen_prof.get_sa():
                self.soft_conflicts += 1
            if new_class.get_course().get_number() not in chosen_prof.get_course_prefs():
                self.course_pref_conflicts += 5
            if not new_class.get_course().get_name() in self.room_times:
                self.room_times[new_class.get_course().get_name()] = [t]
            else:
                for time in self.room_times[new_class.get_course().get_name()]:
                    if(time.check_overlap(t)):
                        self.room_conflicts += 2
                self.room_times[new_class.get_course().get_name()].append(t)

            for dep in new_class.get_course().get_dependencies():
                if dep.get_course().get_name() in self.class_times:
                    if self.class_times[dep.get_course().get_name()].check_overlap(t):
                        self.dependency_conflicts += 5

            if not chosen_prof.get_name() in self.prof_times:
                self.prof_times[chosen_prof.get_name()] = [t]
            else:
                for time in self.prof_times[chosen_prof.get_name()]:
                    if time.check_overlap(t):
                        self.prof_conflicts += 5
                self.prof_times[chosen_prof.get_name()].append(t)


            self.classes.append(new_class)

    def get_classes(self):
        return self.classes

    def add_class(self, c):
        self.classes.append(c)

    def numConflicts(self):
        return self.prof_conflicts + self.room_conflicts + self.dependency_conflicts + self.course_pref_conflicts + self.soft_conflicts

    def check_validity(self):
        if self.numConflicts() != 0:
            return False

        for c in self.classes:
            hard_prefs = c.get_instructor().get_ha()
            if c.get_time() not in hard_prefs:
                return False

        return True

    def get_fitness(self, debug=False):
        conflicts = self.numConflicts()
        return 1/(conflicts + 1)

    def __str__(self):
        s = ""
        for c in self.classes:
            s += str(c) + "\n"
        return s