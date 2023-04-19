import datetime as DT

#13:00, 14:30
class ClassTime():
    def __init__(self, days, time1, time2):
        self.days = days
        self.time1 = DT.datetime.strptime(time1, "%H:%M")
        self.time2 = DT.datetime.strptime(time2, "%H:%M")

    def check_overlap(self, other):
        if self.check_days_overlap(other):
            return self.time1 <= other.time2 and self.time2 >= other.time1
        return False
        
    def check_days_overlap(self, other):
        return ((self.days == "MW" or self.days == "MWF") and (other.days == "MWF" or other.days == "MW")) or (self.days == "TR" and other.days == "TR")
        
    def get_time(self):
        return str(self.days) + "," + str(self.time1)[11:] + ", " + str(self.time2)[11:]

    def __str__(self):
        return str(self.days) + ", " + str(self.time1)[11:] + ", " + str(self.time2)[11:]
    
    def __eq__(self, other):
        return self.days == other.days and self.time1 == other.time1 and self.time2 == other.time2
    
#x = ClassTime('MW','07:00','8:50')
#y = ClassTime('MW','09:00','10:30')
#print(x.check_overlap(y))