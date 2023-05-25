from resources.Data.family_info import FamilyInfo
from resources.Data import SaveFileData
from resources.ABCs.save_method import SaveMethod
from resources.Data.save_file_data import Storage
from resources.util import get_current_date


class TextSaveMethod(SaveMethod):
    def __init__(self, data_source : SaveFileData,  absolute_path: str, file_name: str):
        self.__data_source : SaveFileData = data_source
        self.__absolute_path = absolute_path
        self.__file_name = file_name

    @staticmethod
    def __create_string(data : SaveFileData) -> str:
        print("CREATING STRING" + data.parent, data.children)
        string = f"{data.parent} (Line # {data.line_num}) [File Path: {data.file_path}]\n"
        for child in data.children:
            print(string, child)
            string += "  " + child + "\n"
        #print(string)
        return string

    def save(self):
        content = ""
        with open(f"{self.__absolute_path}{self.__file_name}", "a+") as file:
            content += "~" * 150
            content += f"\nTime Data Added: {get_current_date()}\n"
            print(Storage.storage)
            for data in Storage.retrieve_data():
                content += self.__create_string(data)
            file.write(content)