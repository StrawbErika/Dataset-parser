import os
import json

def ask_direction():
    direction = input("[1] Northbound, [2] Southbound? ")
    if(direction == "1"):
        direction = "northbound"
    elif(direction == "2"):
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
    elif(mr == "2"):
        road = "COMMONWEALTH"
    elif(mr == "3"):
        road = "QUEZON"
    elif(mr == "4"):
        road = "ESPAA"
    elif(mr == "5"):
        road = "C5"
    elif(mr == "6"):
        road = "ORTIGAS"
    elif(mr == "7"):
        road = "MARCOS"
    elif(mr == "8"):
        road = "ROXAS"
    elif(mr == "9"):
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
        # print(main_road)
        if(complete_name[0] == main_road):
            # print(complete_name[0])
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
    while(num != len(list_of_dir)):
        complete_road_data = load_file_into_dict(list_of_dir[num])
        list_of_data.append(complete_road_data[find_road_data_index(complete_road_data,chosen_road)])
        num = num + 1
    return list_of_data

def check_if_empty(list_of_dir):
    not_empty = []
    num = 0
    while(num != len(list_of_dir)):
        if((os.stat(list_of_dir[num]).st_size == 0) == False):
            not_empty.append(list_of_dir[num])
        num = num + 1
    return not_empty

def proper_format_file(filenames, directory):
    file_name = []
    num = 0
    while(num != len(filenames)):
        file_name.append(directory+filenames[num])
        num = num + 1
    return file_name
    
def save_file(data, name):
    file = open(name + ".csv","w") 
    file.write("5 Minutes,Lane 1 Flow (Veh/5 Minutes),# Lane Points,% Observed \n")
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

def convert_time(time):
    hour_minute = ''
    hours = 0
    minute = 0
    if(time[len(time)-2:] == 'pm'):
        list_time = time[0:len(time)-2].split(':')
        hours = int(list_time[0]) + 12
        minute = list_time[1]
    else:
        list_time = time[0:len(time)-2].split(':')
        hours = list_time[0]
        minute = list_time[1]
    return check_format_time(str(hours), "true") + ":" + check_format_time(str(minute), "false")

def convert_all_time(data):
    num = 0
    while(num != len(data)):
        data[num]['time_updated'] = convert_time(data[num]['time_updated']) 
        num = num + 1        
    
def check_format_time(time, hour):
    two_digits = ''
    if(len(time) < 2):
        two_digits = "0" + time
    elif(hour == "true"):
        if(time == "24"):
            two_digits = "00"
        else:
            two_digits = time
    else:
        two_digits = time
    return two_digits

def get_date(directory, index):
    splitted =  directory.split('-')
    sequence_json = splitted[3].split('.')
    seq = sequence_json[0]
    year = seq[:4]
    month = seq[4:6]
    day = seq[6:8]
    complete_date = day+"/"+month+"/"+year 
    return complete_date

def add_to_time(data, directories):
    num = 0
    while(num != len(data)):
        data[num]['time_updated'] = get_date(directories[num], num) + " " + data[num]['time_updated'][:-1]
        num = num + 1        

def format_name(road, direction):
    road_name = road.replace(" ", "_")
    final = direction + "_" + road_name
    return final.lower() 