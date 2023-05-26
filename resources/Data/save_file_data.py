import dataclasses
import typing
from dataclasses import dataclass

@dataclass(frozen=True)
class Storage:
    parent : str
    line_num : int
    children : list[str]
    file_path : str
    save_objs : typing.ClassVar[typing.List['Storage']] = []

    def __post_init__(self):
        Storage.save_objs.append(self)
    @classmethod
    def retrieve_objs(cls):
       for i in cls.save_objs:
           yield i
