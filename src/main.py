import re
import time
import os
import logger

obj_array = []

def options() -> bool:
    selection = input("")
    if selection == '1':
        set_coordinates()
        return True
    elif selection == '2':
        load_coords()
        return True
    elif selection == '3':
        clear_file()
        return True
    elif selection == '4':
        remove_file()
        return True
    elif selection == '5':
        print("quitting...")
        return False
    else: 
        logger.log_msg("Invalid input!", logger.msg_level["error"])
        return True

def main_menu():
    options_loop = True
    while options_loop:
        time.sleep(1)
        print("Welcome to LineGraph!")
        print("Please choose an option: ")
        print("1. Add a set of coordinates to the file")
        print("2. Load the sets of coordinates from a save")
        print("3. Erase all coordinates from the save")
        print("4. Delete the savefile")
        print("5. Quit")
        options_loop = options()


def check_str_for_coords(string):
    # google python regex when you need this again
    ans = re.findall("^(.*[0-9].*,.*[0-9].*)$", string)
    if ans == None:
        logger.log_msg("Line is null!", logger.msg_level["error"])
    else:
        if len(ans) > 1:
            logger.log_msg("More than one set of coordinates found!", logger.msg_level["warn"])
            for i in range (len(ans)):
                print(ans[i])
        elif len(ans) == 0:
            logger.log_msg("Coordinates don't exist!", logger.msg_level["error"])
        else:
            print(ans[0])
            parse_line_as_x_and_y(string)
    

def make_string_of_vars(x, y, is_pushing):
    x = x.strip()
    y = y.strip()
    global coordinate_str 
    coordinate_str = "(" + str(x) + "," + str(y) + ")"
    print(coordinate_str)
    if is_pushing:
        push_to_obj_array(coordinate_str)

def set_coordinates():
    x = input("Please enter an X value: \n")
    y = input("Please enter a Y value: \n")
    make_string_of_vars(x, y, False)
    open_file_and_set_file_type("a", coordinate_str)

def load_coords():
    try:
        file = open("saved.txt", "r")
    except:
        logger.log_msg("File doesn't exist!", logger.msg_level["error"])
    else:
        open_file_and_set_file_type("r", None)

def parse_line_as_x_and_y(line):
    # Add z here when doing 3D
    obj = re.findall(r"\d+", line)
    if len(obj) % 2 != 0:
        logger.log_msg("Invalid number of numbers!", logger.msg_level["error"])
    else:
        for i in range(len(obj)):
            if len(obj) % 2 == 0:
                x = obj[i]
            else:
                y = obj[i]
                make_string_of_vars(x, y, True)

def open_file_and_set_file_type(type, text):
    with open("saved.txt", type) as file:
        if type == 'r':
            check_str_for_coords(file.readline())
        elif type == 'a':
            file.write(text)
        file.close()

def remove_file():
    if os.path.exists("saved.txt"):
        os.remove("saved.txt")
    else:
        logger.log_msg("File doesn't exist!", logger.msg_level["error"])

def clear_file():
    with open("saved.txt", 'w') as file:
        file.write("")
        file.close()

def push_to_obj_array(coord):
    obj_array.append(coord)
    logger.print_msg(obj_array, logger.msg_level["regular"])

def find_sets_of_x_and_y(array):
    for i in range(len(array)):
        obj = re.findall(r"\d+", array[i])
        if i == 0:
            x = obj[0]
            y = obj[1]
        else:
            x2 = obj[0]
            y2 = obj[1]
    find_gradient_of_line(x, y, x2, y2)

def find_gradient_of_line(x1, y1, x2, y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    delta = delta_y / delta_x
    print(delta)

main_menu()