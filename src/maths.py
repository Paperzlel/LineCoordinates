# maths.py is my alternative to import a million maths libraries so I can have better control.
# Lot of number crunching here, watch out

import logger
from tkinter import *

MATHS_SAVED : dict = {
    "MATHS_SAVED_1" : {
        "MATHS_SAVED_X" : 0,
        "MATHS_SAVED_Y" : 0,
        "MATHS_SAVED_LINE_EQUATION" : " "
    },
    "MATHS_SAVED_2" : {
        "MATHS_SAVED_X" : 0,
        "MATHS_SAVED_Y" : 0,
        "MATHS_SAVED_LINE_EQUATION" : " "
    },
    "MATHS_SAVED_3" : {
        "MATHS_SAVED_X" : 0,
        "MATHS_SAVED_Y" : 0,
        "MATHS_SAVED_LINE_EQUATION" : " "
    }
}


def increase_x(xin : int, modifier : int) -> int:
    if not isinstance(modifier, int) or not isinstance(xin, int):
        logger.log_msg("Invalid types input!", 2)
    else:
        global maths_x
        maths_x += xin + 1
        return maths_x

def decrease_x(xin : int, modifier : int) -> int:
    if not isinstance(modifier, int) or not isinstance(xin, int):
        logger.log_msg("Invalid types input!", 2)
    else:
        global maths_x
        maths_x -= xin + 1
        return maths_x

maths_x = MATHS_SAVED["MATHS_SAVED_1"]["MATHS_SAVED_X"]
maths_y = MATHS_SAVED["MATHS_SAVED_1"]["MATHS_SAVED_Y"]