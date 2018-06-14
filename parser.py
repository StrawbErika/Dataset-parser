from functions import *

def get_date(directory):
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
        data[num]['time_updated'] = get_date(directories[num]) + " " + data[num]['time_updated']
        num = num + 1        
    
main_directory = "/home/shortcake/Desktop/OJT/Dataset-parser/out/"
main_road = ask_main_road()
direction =  ask_direction()

directories = proper_format_file(get_files(main_directory), main_directory)
chosen_road = get_chosen_road(main_road, directories)
data = get_all_road_data(main_road, directories, chosen_road)
list_of_direction = get_direction(data, direction)
convert_all_time(list_of_direction)
add_to_time(list_of_direction, directories)
save_file(list_of_direction, chosen_road)