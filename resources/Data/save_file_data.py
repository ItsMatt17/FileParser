import dataclasses
import typing
from dataclasses import dataclass

@dataclass
class DataStorage:
    save_objs : typing.ClassVar[typing.List['SaveFileData']] = []




class Storage:
    storage = []
    def __init__(self, parent : str, line_num : int, children : list[str], file_path : str):
        self.parent = parent
        self.line_num = line_num
        self.children = children
        self.file_path = file_path

        Storage.storage.append(self)

    @classmethod
    def retrieve_data(cls):
        for i in cls.storage:
            print(i.children)
            yield i



@dataclass(frozen=True, eq=False, order=False)
class SaveFileData:
    parent : str
    line_num : int
    children : list[str]
    file_path : str
    save_objs : typing.ClassVar[typing.List['SaveFileData']]

    def __post_init__(self):
        DataStorage.save_objs.append(self)

    @classmethod
    def retrieve_objs(cls):
       for i in DataStorage.save_objs:
           yield i
