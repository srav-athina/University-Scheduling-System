from course_info.meeting_time import ClassTime
class Instructor:
    def __init__(self, name, hard_prefs, soft_prefs, course_prefs, type = None):
        self.name = name #string
        self.hard_prefs = hard_prefs #list
        self.soft_prefs = soft_prefs
        self.course_prefs = course_prefs
        self.type = None
        if type != None:
            self.type = type

    def get_type(self):
        return self.type

    def get_ha(self):
        return self.hard_prefs
    
    def get_sa(self):
        return self.soft_prefs

    def get_course_prefs(self):
        return self.course_prefs

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __hash__(self):
        return hash(self.name)
        
    def get_name(self):
        return self.name
