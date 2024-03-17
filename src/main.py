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
        comp_coord()
        return True
    elif selection == '4':
        clear_file()
        return True
    elif selection == '5':
        remove_file()
        return True
    elif selection == '6':
        print("quitting...")
        return False
    else: 
        logger.log_msg("Invalid input!", 3)
        return True

def main_menu() -> None:
    options_loop = True
    while options_loop:
        time.sleep(1)
        print("Welcome to LineGraph!")
        print("Please choose an option: ")
        print("1. Add a set of coordinates to the file")
        print("2. Load the sets of coordinates from a save")
        print("3. Compile 2 coordinates to an equation")
        print("4. Erase all coordinates from the save")
        print("5. Delete the savefile")
        print("6. Quit")
        options_loop = options()


def check_str_for_coords(string) -> None:
    # google python regex when you need this again
    ans = re.findall("^(.*[0-9].*,.*[0-9].*)$", string)
    if ans == None:
        logger.log_msg("Line is null!", 3)
    else:
        if len(ans) > 1:
            logger.log_msg("More than one set of coordinates found!", 2)
            for i in range (len(ans)):
                print(ans[i])
        elif len(ans) == 0:
            logger.log_msg("Coordinates don't exist!", 3)
        else:
            print(ans[0])
            parse_line_as_x_and_y(string)
    

def make_string_of_vars(x, y) -> None:
    x = x.strip()
    y = y.strip()
    global coordinate_str 
    coordinate_str = "(" + str(x) + "," + str(y) + ")"
    print(coordinate_str)

def set_coordinates() -> None:
    x = input("Please enter an X value: \n")
    y = input("Please enter a Y value: \n")
    make_string_of_vars(x, y)
    open_file_and_set_file_type("a", coordinate_str)

def load_coords() -> None:
    try:
        file = open("saved.txt", "r")
    except:
        logger.log_msg("File doesn't exist!", 3)
    else:
        open_file_and_set_file_type("r", None)

def parse_line_as_x_and_y(line) -> None:
    # Add z here when doing 3D
    obj = re.findall("-*"r"\d+", line)
    if len(obj) % 2 != 0:
        logger.log_msg("Invalid number of numbers!", 3)
    else:
        for i in range (len(obj)):
            if (i + 1) % 2 != 0:
                x = obj[i]
                to_obj_array(x)
            else:
                y = obj[i]
                to_obj_array(y)

def open_file_and_set_file_type(type, text) -> None:
    with open("saved.txt", type) as file:
        if type == 'r':
            check_str_for_coords(file.readline())
        elif type == 'a':
            file.write(text)
        file.close()

def remove_file() -> None:
    if os.path.exists("saved.txt"):
        os.remove("saved.txt")
    else:
        logger.log_msg("File doesn't exist!", 3)

def clear_file() -> None:
    with open("saved.txt", 'w') as file:
        file.write("")
        file.close()

def to_obj_array(item : float):
    obj_array.append(item)

def find_gradient(array) -> float:
    delta_x = float(array[2]) - float(array[0])
    delta_y = float(array[3]) - float(array[1])
    try:
        gradient = delta_y / delta_x
    except:
        logger.log_msg("Division by zero occured!", 3)
        print("Can't divide by zero! Returning to main menu...")
    else:
        return gradient

def find_y_intercept(array) -> float:
    y = float(array[1])
    m = find_gradient(array)
    x = float(array[0])
    c : float = y - (m * x)
    return c

def return_equation(m, c) -> str:
    if c == 0:
        equation_str = "y = " + str(m) + "x"
    elif c < 0:
        equation_str = "y = " + str(m) + "x " + str(c)
    else: 
        equation_str = "y = " + str(m) + "x + " + str(c)
    return equation_str

def comp_coord() -> None:
    obj_array.clear()
    load_coords()
    m = find_gradient(obj_array)
    c = find_y_intercept(obj_array)
    str = return_equation(m, c)
    print("Equation for loaded coordinates is: " + str)

main_menu()