import typing
from abc import ABC, abstractmethod


class ParseStrategy(ABC):
    @abstractmethod
    def parse(self, content : typing.TextIO, file_path : str) -> None:
        ...