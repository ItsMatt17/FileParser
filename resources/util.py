from datetime import datetime
from random import choices

import pytz


def get_current_date() -> str:
    timezone = pytz.timezone('America/New_York')
    time = datetime.now(timezone)
    return time.strftime("%m-%d-%Y | %I:%M %p %Z")


def clear(save_path, save_name) -> None:
    with open(f"{save_path}{save_name}", "w") as file:
        file.write("")

    print("[INFO] File successfully cleared")  # Does not actually check if successful
def gen_random_file_name(save_name) -> str:
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    resp = choices(alpha, k=10)
    return save_name[:-4] + "_" + "".join(resp) + ".txt"

