from functions import *
    
main_directory = "/home/shortcake/Desktop/OJT/Dataset-parser/out/"
main_road = ask_main_road()
print(main_road)
direction =  ask_direction()
directories_unchecked = proper_format_file(get_files(main_directory), main_directory)
directories =  check_if_empty(directories_unchecked)
chosen_road = get_chosen_road(main_road, directories)
data = get_all_road_data(main_road, directories, chosen_road)
list_of_direction = get_direction(data, direction)
convert_all_time(list_of_direction)
add_to_time(list_of_direction, directories)
save_file(list_of_direction, format_name(chosen_road, direction))