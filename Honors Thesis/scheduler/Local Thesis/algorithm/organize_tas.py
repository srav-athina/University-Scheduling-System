from course_info.c import Class
from course_info.instructor import Instructor
from course_info.meeting_time import ClassTime
from data import Data

class ScheduleTAs:
    #change class to hold the 
    def __init__(self, c, requirements):
        self.TAs = c.get_TAs()

    def output_schedule(self):
        pass


c1 = Data.c1
clas = Class(c1)
TAs = ["TA1", "TA2", "TA3", "TA4"]

T1 = [[('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')], 
      [('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')]]
T2 = [[('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')], 
      [('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')]]
T3 = [[('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')], 
      [('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')]]
T4 = [[('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')], 
      [('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')]]

ta_times = [T1, T2, T3, T4]

for i in range(len(TAs)):
    clas.add_TA(Instructor(TAs[i], ClassTime(ta_times[i][0]), ClassTime(ta_times[i][1]), "TA"))

#number of hours required 
requirements = []
test = ScheduleTAs(clas)
test.output_schedule()