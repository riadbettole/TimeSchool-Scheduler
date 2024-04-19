from models.Day import Day
from models.Time import Time
from typing import List

class SlotOfTimeTable:
    def __init__(self):
        pass
    
    def __init__(self, day, hour):
        self.day = day
        self.hour = hour

    def setProfessor(self, prof):
        self.professor = prof
        
    def setGroup(self, grp):
        self.student_group = grp
        
    def setRoom(self, room):
        self.room = room
        
    def setSubject(self, subj):
        self.subject = subj
        
    def setDay(self, day):
        self.day = day
    
    def setHour(self, hour):
        self.hour = hour
        
class TableTime:
    
    def __init__(self, days, times):
        self.days = days
        self.times = times
        self.timeTable : List[List[SlotOfTimeTable]]= self.initializeTimeTable()
        
    def initializeTimeTable(self):
        return [ [SlotOfTimeTable(day=Day(day), hour=Time(time) ) for time in self.times ] for day in self.days ]
    # self.TimeTable = [
    #     [SlotOfTimeTable(Day("mon"),Time("8h-10h")),SlotOfTimeTable(Day("mon"),Time("10h-12h")),SlotOfTimeTable(Day("mon"),Time("14h-16h")),SlotOfTimeTable(Day("mon"),Time("16h-18h"))],
    #     [SlotOfTimeTable(Day("tue"),Time("8h-10h")),SlotOfTimeTable(Day("tue"),Time("10h-12h")),SlotOfTimeTable(Day("tue"),Time("14h-16h")),SlotOfTimeTable(Day("tue"),Time("16h-18h"))],
    #     [SlotOfTimeTable(Day("wed"),Time("8h-10h")),SlotOfTimeTable(Day("wed"),Time("10h-12h")),SlotOfTimeTable(Day("wed"),Time("14h-16h")),SlotOfTimeTable(Day("wed"),Time("16h-18h"))],
    #     [SlotOfTimeTable(Day("thu"),Time("8h-10h")),SlotOfTimeTable(Day("thu"),Time("10h-12h")),SlotOfTimeTable(Day("thu"),Time("14h-16h")),SlotOfTimeTable(Day("thu"),Time("16h-18h"))],
    #     [SlotOfTimeTable(Day("fri"),Time("8h-10h")),SlotOfTimeTable(Day("fri"),Time("10h-12h")),SlotOfTimeTable(Day("fri"),Time("14h-16h")),SlotOfTimeTable(Day("fri"),Time("16h-18h"))],
    #     [SlotOfTimeTable(Day("sat"),Time("8h-10h")),SlotOfTimeTable(Day("sat"),Time("10h-12h")),SlotOfTimeTable(Day("sat"),Time("14h-16h")),SlotOfTimeTable(Day("sat"),Time("16h-18h"))],
    # ]
    # self.TimeTable = [ [[SlotOfTimeTable()] for _ in range(4)] for _ in range(6) ]
    
    def orderUpTheTimeTable():
        pass
    
class TableTimeStudent(TableTime) :
    pass
class TableTimeRoom(TableTime) :
    pass
class TableTimeProfessor(TableTime) :
    pass