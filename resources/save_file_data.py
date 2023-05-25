import typing
from dataclasses import dataclass

from resources.util import get_current_date

@dataclass
class SaveFileData:
    save_objs : typing.ClassVar[list]= []  # So I don't depend on family_info to save
    parent : str
    line_num : int
    children : list[str]
    file_path : str

    def __post_init__(self):
        SaveFileData.save_objs.append(self)
        print(SaveFileData.save_objs)

    def create_string(self) -> str:
        string = f"{self.parent} (Line # {self.line_num}) [File Path: {self.file_path}]\n"
        for child in self.children:
            string += "  " + child + "\n"
        return string
    @classmethod
    def save_data(cls, absolute_path : str, file_name : str):
        content = ""
        with open(f"{absolute_path}{file_name}", "a+") as file:
            content += "~" * 150
            content += f"\nTime Data Added: {get_current_date()}\n"
            for data in cls.save_objs:
                content += data.create_string()
            file.write(content)