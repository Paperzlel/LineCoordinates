import re
import time
import os

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
        print("Error, not a valid option")
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
        print("ERROR: Line is null")
    else:
        if len(ans) > 1:
            print("DEBUG: More than one coordinate in line found!")
            for i in range (len(ans)):
                print(ans[i])
        elif len(ans) == 0:
            print("ERROR: Coordinates don't exist!")
        else:
            print(ans[0])
            parse_line_as_x_and_y(string)
    

def make_string_of_vars(x, y):
    x = x.strip()
    y = y.strip()
    global coordinate_str 
    coordinate_str = "(" + str(x) + "," + str(y) + ")"
    print(coordinate_str)

def set_coordinates():
    second_x = input("Please enter an X value: \n")
    second_y = input("Please enter a Y value: \n")
    make_string_of_vars(second_x, second_y)
    open_file_and_set_file_type("a", coordinate_str)

def load_coords():
    try:
        file = open("saved.txt", "r")
    except:
        print("ERROR: File doesn't exist!")
    else:
        open_file_and_set_file_type("r", None)

def parse_line_as_x_and_y(line):
    # Add z here when doing 3D
    obj = re.findall(r"\d+", line)
    if len(obj) % 2 != 0:
        print("ERROR: Coordinates are in an invalid quantity!")
    else:
        for i in range(len(obj)):
            if len(obj) % 2 == 0:
                x = obj[i]
            else:
                y = obj[i]
                make_string_of_vars(x, y)

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
        print("ERROR: File does not exist!")

def clear_file():
    with open("saved.txt", 'w') as file:
        file.write("")
        file.close()

main_menu()