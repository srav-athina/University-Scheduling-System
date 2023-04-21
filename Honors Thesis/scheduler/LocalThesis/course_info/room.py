class Room:
    def __init__(self, location, room):
        self.location = location
        self.room = room

    def get_room(self):
        return self.room

    def get_location(self):
        return self.location
    
    def __str__(self):
        return self.location + ", " + self.room

#r = Room('Oak Hall', '306')
#print(r.get_room())
#print(r.get_location())
#print(r)