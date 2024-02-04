import re
import time

def options():
    selection = input("")
    if selection == '1':
        set_coordinates()
        return True
    elif selection == '2':
        load_coords()
        return True
    elif selection == '3':
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
        print("1. Set coordinates")
        print("2. Load coordinates from save")
        print("3. Quit")
        options_loop = options()


def check_str_for_coords(string):
    # google python regex when you need this again
    ans = re.search("^(.*[0-9].*,.*[0-9].*)$", string)
    print(ans)
    if ans:
        print("String is a set of coordinates with numbers")
        parse_line_as_x_and_y(string)
    else:
        print("String doesn't contain a set of coordinates :(")
    

def make_string_of_vars(x, y):
    x = x.strip()
    y = y.strip()
    global coordinate_str 
    coordinate_str = "(" + str(x) + "," + str(y) + ")"
    print(coordinate_str)

def set_coordinates():
    x = input("Please enter an x value: \n")
    y = input("Please enter a y value: \n")
    make_string_of_vars(x, y)
    open_file_and_set_file_type("w", coordinate_str)

def load_coords():
    try:
        file = open("saved.txt", "x")
    except:
        print("DEBUG: File already exists")
    else:
        open_file_and_set_file_type("r", None)
    finally:
        open_file_and_set_file_type("r", None)

def parse_line_as_x_and_y(line):
    obj = re.findall(r"\d+", line)
    x = obj[0]
    y = obj[1]
    # Add z here when doing 3D
    make_string_of_vars(x, y)

def open_file_and_set_file_type(type, text):
    with open("saved.txt", type) as file:
        if type == 'r':
            check_str_for_coords(file.readline())
        elif type == 'w':
            file.write(text)
        file.close()
        
main_menu()