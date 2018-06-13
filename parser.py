import os
import json

def ask_direction():
    direction = input("Northbound, Southbound? ")
    if(direction.lower() == "northbound"):
        direction = "northbound"
    elif(direction.lower() == "southbound"):
        direction = "southbound"
    else:
        print("error direction")
    return direction

def get_files(directory):
    return os.listdir(directory)
    
def ask_main_road():
    mr = input("[1] EDSA\n [2] Commonwealth \n [3] Quezon ave\n [4] Espana\n [5] C5\n [6] Ortigas\n [7] Marcos highway\n [8] Roxas blvd\n [9] SLEX\n  ")
    road = ""
    if(mr == "1"):
        road = "EDSA"
    elif(road == "2"):
        road = "COMMONWEALTH"
    elif(road == "3"):
        road = "QUEZON"
    elif(road == "4"):
        road = "ESPAA"
    elif(road == "5"):
        road = "C5"
    elif(road == "6"):
        road = "ORTIGAS"
    elif(road == "7"):
        road = "MARCOS"
    elif(road == "8"):
        road = "ROXAS"
    elif(road == "9"):
        road = "SLEX"
    return road

def load_file_into_dict(file_name):
    file = open(file_name, "r") 
    contents = file.read()
    file.close()
    contents_dict = json.loads(contents)
    return contents_dict

def road_names(main_road, road_data):
    print(main_road)
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

def ask_sub_road():
    sub = input("Choose from above:")
    return int(sub)

def find_road_data_index(complete_road_data, name):
    num = 0
    while(num != len(complete_road_data)):
        if(complete_road_data[num]["line"] == name):
            print(num)
            index = num 
        num = num + 1
    return index


complete_road_data = load_file_into_dict("/home/shortcake/Desktop/OJT/Dataset-parser/out/traffic-status-20180530000000.json")
main_road = ask_main_road()
direction =  ask_direction()
sub_roads = road_names(main_road, complete_road_data)
sub_road_index = ask_sub_road()
chosen_road = sub_roads[sub_road_index]
road_data = complete_road_data[find_road_data_index(complete_road_data,chosen_road)]
print(road_data)
