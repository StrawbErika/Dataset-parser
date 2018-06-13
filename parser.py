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
            index = num 
        num = num + 1
    return index

def get_chosen_road(main_road, list_of_dir):
    road_data = load_file_into_dict(list_of_dir[0])
    sub_roads = road_names(main_road, road_data)
    sub_road_index = ask_sub_road()
    chosen_road = sub_roads[sub_road_index]
    return chosen_road

def get_all_road_data(main_road, list_of_dir, chosen_road):
    list_of_data = []
    num = 0
    fake = 0
    while(num != len(list_of_dir)):
        if((check_if_empty(list_of_dir[num])) == False):
            complete_road_data = load_file_into_dict(list_of_dir[num])
            list_of_data.append(complete_road_data[find_road_data_index(complete_road_data,chosen_road)])
        else:
            fake = fake + 1
        num = num + 1
    return list_of_data

def check_if_empty(file):
    boolean = (os.stat(file).st_size == 0)
    return boolean

def proper_format_file(filenames, directory):
    file_name = []
    num = 0
    while(num != len(filenames)):
        file_name.append(directory+filenames[num])
        num = num + 1
    return file_name
    
def save_json(data, name):
    file = open(name + ".csv","w") 
    file.write("30 Minutes,Lane 1 Flow (Veh/30 Minutes),# Lane Points,% Observed \n")
    num = 0
    while(num != len(data)):
        file.write(data[num]['time_updated'] + "," + get_status(data[num]["status"]) + "," + "1" + "," + "100" + "\n")
        num = num + 1        
    file.close() 

def get_status(status):
    num = 0
    if(status == "light"):
        num = 25
    elif(status == "mod"):
        num = 50
    else:
        num = 75
    return str(num)

def get_direction(data, direction):
    direction_data = []
    num = 0
    while(num != len(data)):
        hello = data[num][direction]
        direction_data.append(hello)
        num = num + 1
    return direction_data
    
main_directory = "/home/shortcake/Desktop/OJT/Dataset-parser/out/"
main_road = ask_main_road()
direction =  ask_direction()

directories = proper_format_file(get_files(main_directory), main_directory)
chosen_road = get_chosen_road(main_road, directories)
data = get_all_road_data(main_road, directories, chosen_road)
list_of_direction = get_direction(data, direction)
save_json(list_of_direction, chosen_road)