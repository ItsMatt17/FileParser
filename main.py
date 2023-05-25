from typing import Final
from pathlib import Path
from resources import Directory, FileParser

from resources.Data import SaveFileData, FamilyInfo
from resources.Strategies import TextSaveMethod, ChildTermAfterMonthStrategy
from resources.util import gen_random_file_name, clear

RANDOM_FILE_NAME_GEN : bool = False
CLEAR_MODE = True # You won't need
PATH : Final[str] = "./test_files/nested_test"  # Must be parent folder
SAVE_PATH : Final[str] = "./"  # Always end with a /
SAVE_NAME : Final[str] = "script_save_data.txt"

#BUG: Fix incorrect output
#BUG: Fix


def main():
    file_name = SAVE_NAME  # Yes I know this is a dumb asf way of doing this

    if CLEAR_MODE:
        clear(SAVE_PATH, SAVE_NAME)

    if RANDOM_FILE_NAME_GEN:
        file_name = gen_random_file_name(SAVE_NAME)


    directory = Directory(Path(PATH))
    file_info = FileParser(directory=directory, strategy=ChildTermAfterMonthStrategy(FamilyInfo(SaveFileData)))
    file_info.iter_folders()

    save_method = TextSaveMethod(data_source=SaveFileData, absolute_path=SAVE_PATH, file_name=file_name)
    save_method.save()



if __name__ == "__main__":
    main()