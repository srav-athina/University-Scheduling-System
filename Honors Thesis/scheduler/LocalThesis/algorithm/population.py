import sys
sys.path.append("C:\\Users\\jnaat\\OneDrive\\Documents\\School\\Thesis\\Honors Thesis\\scheduler\\LocalThesis")
from algorithm.schedule import Schedule

class Population:
    def __init__(self, size, courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms):
        self.size = size
        self.schedules = []
        for i in range(size):
            self.schedules.append(Schedule(courses, dependencies, profs, hard_prefs, soft_prefs, course_prefs, rooms))
        self.viable_schedules = []

    def get_schedules(self):
        return self.schedules

    def get_viable_schedules(self):
        for schedule in self.schedules:
            if schedule.check_validity():
                self.viable_schedules.append(schedule)
        return self.viable_schedules

    def __iter__(self):
        return iter(self.schedules)

    def __len__(self):
        return len(self.schedules)
    
#git add .
#git commit
#comment something - esc - :wq
#git push origin master