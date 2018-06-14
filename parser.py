from functions import *

main_directory = "/home/shortcake/Desktop/OJT/Dataset-parser/out/"
main_road = ask_main_road()
direction =  ask_direction()

directories = proper_format_file(get_files(main_directory), main_directory)
chosen_road = get_chosen_road(main_road, directories)
data = get_all_road_data(main_road, directories, chosen_road)
list_of_direction = get_direction(data, direction)
convert_all_time(list_of_direction)
save_file(list_of_direction, chosen_road)