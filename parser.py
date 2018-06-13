import os

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
        direction = "Commonwealth"
    elif(direction.lower() == "quezon ave"):
        direction = "Quezon ave"
    elif(direction.lower() == "espana"):
        direction = "Espana"
    elif(direction == "C5"):
        direction = "C5"
    elif(direction.lower() == "ortigas"):
        direction = "Ortigas"
    elif(direction.lower() == "marcos highway"):
        direction = "Marcos highway"
    elif(direction.lower() == "roxas blvd"):
        direction = "Roxas blvd"
    elif(direction.lower() == "slex"):
        direction = "SLEX"
    else:
        print("error main road")
    return main_road


