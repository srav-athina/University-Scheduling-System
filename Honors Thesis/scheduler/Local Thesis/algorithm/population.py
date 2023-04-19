from algorithm.schedule import data
from algorithm.schedule import Schedule

class Population:
    def __init__(self, size):
        self.size = size
        self.schedules = []
        for i in range(size):
            self.schedules.append(Schedule().create())
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
