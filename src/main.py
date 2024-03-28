# main.py is made to load code from the rest of the programs to present to the user.
# This includes saving and loading of each local file's permanent dictionaries
# More uses later down the line

import logger
import json
import gui
import maths

obj_array = []

MAIN_SAVE : dict = {
    "MATHS_SAVED" : maths.MATHS_SAVED,
    "WINDOW_PREFERENCES" : gui.WINDOW_PREFERENCES
}

def save_user_preferences() -> None:
    json_obj = json.dumps(MAIN_SAVE, indent=4)
    with open("SAVE.json", "w") as outfile:
        outfile.write(json_obj)

def load_user_preferences() -> dict:
    with open("SAVE.json", "r") as file:
        json_obj = json.load(file)
    file.close()
    return json_obj

def initialise() -> None:
    # TODO: add stuff
    pass