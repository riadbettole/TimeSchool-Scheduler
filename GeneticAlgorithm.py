from typing import List
from models.Professor import Professor
from models.Room import Room
from models.Subject import Subject
from TimeTable import TableTime, SlotOfTimeTable
import random 

class GeneticAlgorithm:
    def __init__(self, lop):#, lor, los):  
        self.days = ["mon", "tue", "wed", "thu", "fri", "sat"]
        self.times = ["8h-10h", "10h-12h", "14h-16h", "16h-18h"]
        self.TimeTable = TableTime(self.days, self.times)#.initializeTimeTable(self.days, self.times)
              
        self.list_of_professors : List[Professor] = lop 
        #self.list_of_rooms : List[Room] = lor
        #self.list_of_subjects : List[Subject] = los
        self.randomizeDataInSlot()
        

    def initializeAllOfSlots():
        pass
    
    def randomizeDataInSlot(self):
        available_professors_per_day = self.linearProfessor()
        # print(available_professors_per_day["mon"][0])
        for i in range(6): #days
            for j in range(4):
                slot_of_time_table = self.TimeTable.timeTable[i][j]
                available_professor = self.chooseRandomProfessor(available_professors_per_day[str(slot_of_time_table.day)])  

                self.TimeTable.timeTable[i][j].setProfessor(available_professor)
                        
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
        linear = []
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
        linear = []
        linear = {day:[] for day in self.days}
        for professor in self.list_of_professors: 
            availability = professor.availability
            for day in availability:
                for _ in range(availability[day]["nbr_of_possible_classes_day"]):#howmuchtimes:
                    linear[day].append(professor) #should add the prof x times
        return linear
    
    def chooseRandomRoom(self, available_professors_this_day):
        selected_professor = random.choice(available_professors_this_day)
        available_professors_this_day.remove(selected_professor)
        return selected_professor