from datetime import datetime

msg_level = {
    "regular": 0,
    "debug": 1,
    "warning": 2,
    "error": 3
}

def log_msg(text, level):
    user_time = datetime.now()
    with open("log.txt", 'a') as file:
        if level == 1:
            file.write("[At " + str(user_time) + "]: DEBUG: " + text + "\n")
        elif level == 2:
            file.write("[At " + str(user_time) + "]: WARN: " + text + "\n")
        elif level == 3:
            file.write("[At " + str(user_time) + "]: ERROR: " + text + "\n")
