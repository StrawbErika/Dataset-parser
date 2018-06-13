import os
import json

def ask_direction():
    direction = input("Northbound, Southbound? ")
    if(direction.lower() == "northbound"):
        direction = "Northbound"
    elif(direction.lower() == "southbound"):
        direction = "Southbound"
    else:
        print("error direction")
    return direction

def get_files(directory):
    return os.listdir(directory)
    
def ask_main_road():
    main_road = input("EDSA\n Commonwealth \n Quezon ave\n Espana\n C5\n Ortigas\n Marcos highway\n Roxas blvd\n SLEX\n  ")
    if(direction.lower() == "edsa"):
        direction = "EDSA"
    elif(direction.lower() == "commonwealth"):
        direction = "COMMONWEALTH"
    elif(direction.lower() == "quezon ave"):
        direction = "QUEZON"
    elif(direction.lower() == "espana"):
        direction = "ESPAA"
    elif(direction == "C5"):
        direction = "C5"
    elif(direction.lower() == "ortigas"):
        direction = "ORTIGAS"
    elif(direction.lower() == "marcos highway"):
        direction = "MARCOS"
    elif(direction.lower() == "roxas blvd"):
        direction = "ROXAS"
    elif(direction.lower() == "slex"):
        direction = "SLEX"
    else:
        print("error main road")
    return main_road

def load_file_into_dict(file_name):
    file = open(file_name, "r") 
    contents = file.read()
    file.close()
    contents_dict = json.loads(contents)
    return contents_dict

def road_names(main_road, road_data):
    list_road_names = []
    num = 0
    x = 0
    while(num != len(road_data)):
        complete_name = road_data[num]["line"].split(" ")
        if(complete_name[0] == main_road):
            list_road_names.append(road_data[num]["line"])
            print("[" + str(x) + "] " +road_data[num]["line"])
        x = x + 1
        num = num + 1
    return list_road_names

complete_road_data = load_file_into_dict("/home/shortcake/Desktop/OJT/Dataset-parser/out/traffic-status-20180530000000.json")
road_names("COMMONWEALTH", complete_road_data)
