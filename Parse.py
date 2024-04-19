import json
from typing import List
from models.Professor import Professor
from models.Room import Room
from models.Subject import Subject
from models.Day import Day
from models.Time import Time

def parse(path):
    with open(path, "r+") as my_data:
        parsedProfData = json.load(my_data)
    return parsedProfData

def parseProfessor(path):
    list_of_parsed_professors = parse(path)
    list_of_professors : List[Professor] = []
    
    for professor in list_of_parsed_professors:
        nbr_of_possible_classes = 0
        name = professor
        
        availabilityDict = list_of_parsed_professors[professor]["availability"]
        list_of_professionsDict = list_of_parsed_professors[professor]["list_of_professions"]
        
        availability = { day:{"hours":[Time(hour) for hour in availabilityDict[day]]} for day in availabilityDict }
        
        for day in availability:
            nbr_of_possible_classes_day = 0
            for _ in availability[day]["hours"]:
                nbr_of_possible_classes += 1 
                nbr_of_possible_classes_day += 1
            availability[day]["nbr_of_possible_classes_day"] = nbr_of_possible_classes_day  
            
        list_of_professions = list_of_professionsDict
        list_of_professors.append(Professor(name=name, avail=availability, lprof=list_of_professions, nbr_of_possible_classes=nbr_of_possible_classes))

    # for n in list_of_professors:
    #     print("Professor name = ",n.professor_name)
    #     for day in n.availability:
    #         print("Day = ",day)
    #         for time in n.availability[day]["hours"]:
    #             print("Time = ",time)
    #         print("Max teacher can do : ", n.availability[day]["nbr_of_possible_classes_day"])
        
    return list_of_professors
            
def parseRooms(path):
    list_of_parsed_rooms = parse(path + "/rooms.json")
    list_of_rooms : List[Room] = [] 
    for room in list_of_parsed_rooms:
        room_name = room
        capacity = list_of_parsed_rooms[room]["nbr_place"]
        has_computers = list_of_parsed_rooms[room]["has_computer"]
        list_of_rooms.append(Room(room_name, capacity, has_computers))
    return list_of_rooms

def parseSubjects(path):
    # list_of_subjects
    # return parsedSubjects
    pass
    
def parseInfos(path):
    list_of_professors = parseProfessor(path + "/professors.json")
    list_of_rooms = parse(path + "/rooms.json")
    # list_of_subjects = parse(path + "/subjects.json")
    return list_of_professors, list_of_rooms#, list_of_subjects