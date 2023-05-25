import typing

from resources import FamilyInfo, Directory
from resources.ABCs.ParseStrategy import ParseStrategy


class ChildTermAfterMonthStrategy(ParseStrategy):

    def __init__(self, family : FamilyInfo):
        self.__family : FamilyInfo = family

    @staticmethod
    def __is_parent(text: str):
        return text.upper()[2:5] == 'IND'

    def __unique_child_check(self, text: str):

        if text[:5].upper() != "ACLDM":
            return

        if len(text) < 125:
            return

        print(text[124])
        if text[124].upper() == "D":
            self.__family.found_unique_child()
            return

        if len(text) < 603:
            return

        try:
            if text[602] is not None:  # In case 611 goes out of bounds (prob won't need in real files)
                self.__family.found_unique_child()
                return

            if text[602:611] is not None:
                self.__family.unique_child_found = True
                return
        except IndexError as e:
            print(e)

    def parse(self, content : typing.TextIO, file_path : str ):
        final_line_num = 1
        for line_num, text in enumerate(content.readlines()):
            final_line_num = line_num
            text = text.replace("\n", "")
            if self.__family.parent and not self.__is_parent(text):
                # Current parent saved & text is not parent
                self.__unique_child_check(text)
                self.__family.add_child(text)

            elif self.__is_parent(text):
                # New Parent Found
                self.__family.new_parent(text, line_num + 1,
                                         file_path)  # Might be a bad way to send file location | Fix later if needed

            else:
                print("Fucky Wucky")

        print(f"Final line number for {file_path} is #{final_line_num}")
