import sys
#print(sys.path)
sys.path.append("C:\\Users\\jnaat\\OneDrive\\Documents\\School\\Thesis\\Honors Thesis\\scheduler\\LocalThesis")

from algorithm.schedule import Schedule
from algorithm.population import Population

import random as rnd
import numpy as np
from course_info.room import Room
from course_info.instructor import Instructor
from course_info.course import Course
from course_info.meeting_time import ClassTime

POPULATION_SIZE = 1000
MUTATION_RATE = 0.05
MAX_ITERATIONS = 1000

class GeneticAlg:
    def evolve_population(self, population, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms):
        return self.mutate_population(self.crossover_population(population, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms), courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms)
    
    def mutate_population(self, population, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms):
        for schedule in population:
            self.mutate_schedule(schedule, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms)
        return population

    def crossover_population(self, population, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms):
        crossover_pop = Population(0, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms)

        fitnesses = [schedule.get_fitness() for schedule in population]
        prob_sum = sum(fitnesses)
        probabilities = [fitness/prob_sum for fitness in fitnesses]

        for i in range(POPULATION_SIZE):
            # based on the fitness, select schedules for population 
            schedule1 = np.random.choice(population.get_schedules(), 1, p = probabilities)[0]
            schedule2 = np.random.choice(population.get_schedules(), 1, p = probabilities)[0]
            while schedule1 == schedule2:
                schedule2 = np.random.choice(population.get_schedules(), 1, p = probabilities)[0]
            crossover_pop.get_schedules().append(self.mate_schedules(schedule1, schedule2, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms))
        return crossover_pop

    def mate_schedules(self, sched1, sched2, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms):
        crossover_sched = Schedule(courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms)
        for i in range(len(crossover_sched.get_classes())):
            if rnd.random() > 0.5:
                crossover_sched.get_classes()[i] = sched1.get_classes()[i]
            else:
                crossover_sched.get_classes()[i] = sched2.get_classes()[i]
        return crossover_sched
    
    # make a change and output another sched
    def mutate_schedule(self, mutate_schedule, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms):
        #sched = Schedule(courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms)
        sched = None
        for i in range(len(mutate_schedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                if sched is None:
                    sched = Schedule(courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms)
                mutate_schedule.get_classes()[i] = sched.get_classes()[i]
        return mutate_schedule

    def run(self, courses, dependencies, profs, hard_prefs_inputs, soft_prefs_inputs, course_pref, room_inputs):
        #pop will take in data and make sched
        course_prefs = []
        for i in range(len(course_pref)):
            course_prefs.append([])
            for j in range(len(course_pref[i])):
                course_prefs[i].append("CSE" + course_pref[i][j])
        
        course_profs = {}
        for i in range(len(course_prefs)):
            for course in course_prefs[i]:
                if course in course_profs:
                    course_profs[course].append(i)
                else:
                    course_profs[course] = [i]

        rooms = [Room(room[0], room[1]) for room in room_inputs]


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


        instructors = [Instructor(profs[i], hard_times[i], soft_times[i], course_prefs[i]) for i in range(len(profs))]

        courses = [Course(value[0]+key, value[1], [instructors[i] for i in course_profs[value[0]+key]], value[2]) for key, value in courses.items()]

        for c1 in courses:
            for c2 in courses:
                if c1.get_number() in dependencies and c2.get_number() in dependencies[c1.get_number()]:
                    c1.add_dependencies(c2)

        population = Population(POPULATION_SIZE, courses, dependencies, instructors, hard_times, soft_times, course_prefs, rooms)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        generation = 0

        print("generation: " + str(generation) + ", fitness:", population.get_schedules()[0].get_fitness())
        print(population.get_schedules()[0])

        while population.get_schedules()[0].get_fitness() != 1.0 and generation < MAX_ITERATIONS:
            generation += 1
            population = self.evolve_population(population, courses, dependencies, instructors, hard_times, soft_times, course_prefs, rooms)
            population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

            best = population.get_schedules()[0]
            print("generation: " + str(generation) + ", fitness:", population.get_schedules()[0].get_fitness())
            print("soft conflicts: " + str(best.soft_conflicts) + ", course_pref_conflicts: " + str(best.course_pref_conflicts) + ", room_conflicts: " + str(best.room_conflicts) + ", dependency_conflicts: " + str(best.dependency_conflicts) + ", prof_conflicts: " + str(best.prof_conflicts))
            print(population.get_schedules()[0])
            print("There are " + str(len(population.get_viable_schedules())) + " viable schedules at the moment.\n")