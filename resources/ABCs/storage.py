from dataclasses import dataclass
from typing import Protocol

@dataclass
class Storage(Protocol):

    @classmethod
    def retrieve_objs(cls):
        ...