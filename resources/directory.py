import typing
from pathlib import Path

class Directory:
    def __init__(self, path_obj : Path):
        self.__path : Path = path_obj
        self.__current_file = None

    def walk_path(self, search_pattern : str="*.insert") -> typing.Iterable[Path]:
        for file in self.__path.rglob(search_pattern):
            self.__current_file = file.absolute()
            yield file

    @property
    def get_path(self):
        return self.__path

    @property
    def current_file_path(self) -> Path:
        return self.__current_file