# gui.py is for all of the GUI stuff that goes on (duh)
# This is mainly drawing to the window and user input (as I'm moving away from command-line stuff for now)
# This script will be reliant on the rest of the program to give sufficent input

import logger
import maths
from tkinter import *
from tkinter import ttk

WINDOW_PREFERENCES : dict = {
    "WINDOW_NAME_PREFERENCE" : "LineGraph",
    "WINDOW_SIZE_PREFERENCES" : {
        "WINDOW_SIZE_MAX_X" : 1920,
        "WINDOW_SIZE_MAX_Y" : 1080, # Implement higher values here :)
        "WINDOW_SIZE_USER_X" : 1280,
        "WINDOW_SIZE_USER_Y" : 720
    }
}
gui_x : int = 0

def new_window() -> None:
    global window

    window = Tk()
    window.title(WINDOW_PREFERENCES["WINDOW_NAME_PREFERENCE"])

    window.geometry(geometry_parser(
        WINDOW_PREFERENCES["WINDOW_SIZE_PREFERENCES"]["WINDOW_SIZE_USER_X"], 
        WINDOW_PREFERENCES["WINDOW_SIZE_PREFERENCES"]["WINDOW_SIZE_USER_Y"]))
    window.maxsize(
        WINDOW_PREFERENCES["WINDOW_SIZE_PREFERENCES"]["WINDOW_SIZE_MAX_X"], 
        WINDOW_PREFERENCES["WINDOW_SIZE_PREFERENCES"]["WINDOW_SIZE_MAX_Y"])
    
    frame = Frame(window, width=200, height=200)
    frame.pack()
    
    global x_box
    x_box = Label(frame, text="testing lol")
    x_box.place(x=50, y=25)
    x_box.pack()

    x_increase_button = ttk.Button(window, text="+", command=lambda: change_x(gui_x, '+'))
    x_increase_button.place(x=50, y=50)

    x_decrease_button = ttk.Button(window, text="-", command=lambda: change_x(gui_x, '-'))
    x_decrease_button.place(x=50, y=75)
    

    window.mainloop()

def geometry_parser(window_x, window_y) -> str:
    geometry_str = str(window_x) + "x" + str(window_y)
    return geometry_str

def change_x(xin : int, type : str) -> None:
    if type == '+':
        gui_x = maths.increase_x(xin, 1)
        edit_x_in_gui(gui_x)
    elif type == '-':
        gui_x = maths.decrease_x(xin, 1)
        edit_x_in_gui(gui_x)
    else:
        logger.log_msg("Invalid x change type!", 3)
    print("test", gui_x)

def edit_x_in_gui(value) -> None:
    n_val = str(value)
    global x_box
    x_box.config(text = n_val)

new_window()