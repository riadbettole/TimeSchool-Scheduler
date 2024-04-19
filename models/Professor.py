from typing import Dict, List
from .Day import Day

class Professor:
    def __init__(self, name, avail, lprof, nbr_of_possible_classes):
        self.professor_name = name
        self.availability: Dict[Day] = avail
        self.list_of_professions = lprof
        self.number_of_possible_classes  = nbr_of_possible_classes
        
    def __str__(self) -> str:
        # return str(self.availability["mon"]["hours"][0])
        text = ""
        text += "Professor name = " + self.professor_name + '\n'
        for day in self.availability:
            text += "Day = " + day + '\n'
            for i in range(self.availability[day]["nbr_of_possible_classes_day"]):
                text += "Time = " + str(self.availability[day]["hours"][i]) + '\n'
            text += "Max teacher can do : "+ str(self.availability[day]["nbr_of_possible_classes_day"]) + '\n'
        return text