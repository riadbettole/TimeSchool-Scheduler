from GeneticAlgorithm import GeneticAlgorithm
from Parse import parseInfos

if __name__ == '__main__':
    # list_of_professors, list_of_rooms , list_of_subjects = parseInfos("data")
    list_of_professors, list_of_rooms = parseInfos("data")
    
    Gen = GeneticAlgorithm(list_of_professors, list_of_rooms)#, list_of_subjects)
    # Gen.initializeAllAssignementOfSlot()

    # table_time = {
    #     "lundi":{
    #             "8:10":[],
    #             "10:12":[],
    #             "14:16":[],
    #             "16:18":[],
    #         },
    #     "mardi":{
    #             "8:10":[],
    #             "10:12":[],
    #             "14:16":[],
    #             "16:18":[],
    #         },
    #     "mercredi":{
    #             "8:10":[],
    #             "10:12":[],
    #             "14:16":[],
    #             "16:18":[],
    #         },
    #     "jeudi":{
    #             "8:10":[],
    #             "10:12":[],
    #             "14:16":[],
    #             "16:18":[],
    #         },
    #     "vendredi":{
    #             "8:10":[],
    #             "10:12":[],
    #             "14:16":[],
    #             "16:18":[],
    #         },
    #     "samedi":{
    #             "8:10":[],
    #             "10:12":[],
    #             "14:16":[],
    #             "16:18":[],
    #         },
    # }