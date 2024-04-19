from typing import List, Dict
from models.Professor import Professor
from models.Room import Room
from models.Subject import Subject
from TimeTable import TableTime, SlotOfTimeTable
import random 
import time

class GeneticAlgorithm:
    def __init__(self, lop, lor):#, los):  
        self.days = ["mon", "tue", "wed", "thu", "fri", "sat"]
        self.hours = ["8h-10h", "10h-12h", "14h-16h", "16h-18h"]
        self.TimeTable = TableTime(self.days, self.hours)#.initializeTimeTable(self.days, self.times)
              
        self.list_of_professors : List[Professor] = lop 
        self.list_of_rooms : List[Room] = lor
        #self.list_of_subjects : List[Subject] = los
        self.randomizeDataInSlot()
        

    def initializeAllOfSlots():
        pass
    
    def randomizeDataInSlot(self):
        available_professors_per_day = self.linearProfessor()
        available_room_per_day_and_hour = self.linearRoom()
        # print(available_room_per_day_and_hour)
        # print(available_professors_per_day["mon"][0])
        for i in range(6): #days
            for j in range(4):
                slot_of_time_table = self.TimeTable.timeTable[i][j]
                available_professor : Professor= self.chooseRandomProfessor(available_professors_per_day[str(slot_of_time_table.day)])  
                available_room : Room= self.chooseRandomRoom(available_room_per_day_and_hour, available_professor)
                print(available_room)
                
                self.TimeTable.timeTable[i][j].setProfessor(available_professor)
                self.TimeTable.timeTable[i][j].setRoom(available_room)
                #can't really force the room to be with computers, its gonna be a soft contraint
                hour_slot.setSubject(self.list_of_subjects[RANDOM])
            # 
            # print(available_professor)
            # pass
                
                
                # available_room
                # available_group
                # available_subject
        
                # hour_slot.setGroup(self.list_of_groups[RANDOM])
                # hour_slot.setRoom(self.list_of_rooms[RANDOM])
                # hour_slot.setSubject(self.list_of_subjects[RANDOM])
        

    #we have professors and they are available for lets say 4 times, 
    #we make it so that we have his name 4 times and remove it each time hes assigned
    def linearProfessor(self): 
        linear = {day:[] for day in self.days}
        for professor in self.list_of_professors: 
            availability = professor.availability
            for day in availability:
                for _ in range(availability[day]["nbr_of_possible_classes_day"]):#howmuchtimes:
                    linear[day].append(professor) #should add the prof x times
        return linear
    
    def chooseRandomProfessor(self, available_professors_this_day):
        selected_professor = random.choice(available_professors_this_day)
        available_professors_this_day.remove(selected_professor)
        return selected_professor
        
    def linearRoom(self): 
        linear = {day:{} for day in self.days}
        for day in self.days:
            for room in self.list_of_rooms:
                linear[day][room] = [hour for hour in self.hours]
        return linear
    
    def chooseRandomRoom(self, available_rooms_this_day_and_time: Dict, available_professor : Professor):
        days = [days for days in available_professor.availability]
        found = False
        while not found:
            selected_day = random.choice(days)
            selected_room = random.choice(list(available_rooms_this_day_and_time[selected_day].keys()))
            if selected_room not in available_rooms_this_day_and_time[selected_day]:
                days.remove(selected_day)
            else:
                found = True
        
        hours = available_rooms_this_day_and_time[selected_day][selected_room]
        selected_hour = random.choice(hours)
                                                            

        available_rooms_this_day_and_time[selected_day][selected_room].remove(selected_hour)
        
        if len(available_rooms_this_day_and_time[selected_day][selected_room]) == 0:
            available_rooms_this_day_and_time[selected_day].pop(selected_day)
        
        return selected_room
    
    
    