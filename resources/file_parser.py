import typing

import pathlib

from resources.save_file_data import SaveFileData
from resources.family_info import FamilyInfo
from resources.directory import Directory
class FileParser:
    def __init__(self, directory : Directory, family):
        #~~~~~~~~ Dependencies ~~~~~~~~~
        self.__directory : Directory = directory
        self.__path : pathlib.Path = self.__directory.get_path
        self.__save_method = SaveFileData

        #~~~~~~~~ Family Data ~~~~~~~~~
        self.__family : FamilyInfo = family(self.__save_method)

    def iter_folders(self):
        PATH_TO_WALK = self.__directory.walk_path()

        file : pathlib.Path
        for file_count, file in enumerate(PATH_TO_WALK):
            print(f"Currently on file: {file_count + 1} | File Path: {self.__directory.current_file_path}")
            with file.open() as f:
                self.read_file(f)

    @staticmethod
    def is_parent(text : str):
        return text.upper()[2:5] == 'IND'

    def unique_child_check(self, text : str):
        if text.upper()[:5]!= "ACLDM":
            return

        if len(text) < 125:
            return

        if text[124].upper() == "D":
            self.__family.unique_child_found = True
        if len(text) < 603:
            return

        try:
            if text[602] is not None:  #In case 611 goes out of bounds (prob won't need in real files)
                self.__family.unique_child_found = True
                return

            if text[602:611] is not None:
                self.__family.unique_child_found = True
                return
        except IndexError as e:
            print(e)

    def read_file(self, content : typing.TextIO):
        final_line_num = 1
        for line_num, text in enumerate(content.readlines()):
            final_line_num = line_num
            text = text.replace("\n", "")
            if self.__family.parent and not self.is_parent(text):
                # Current parent saved & text is not parent
                self.unique_child_check(text)
                self.__family.add_child(text[:5])

            elif self.is_parent(text):
                # New Parent Found
                self.__family.new_parent(text, line_num + 1, str(self.__directory.current_file_path))  # Might be a bad way to send file location | Fix later if needed

        print(f"Final line number for {self.__directory.current_file_path} is #{final_line_num}")

