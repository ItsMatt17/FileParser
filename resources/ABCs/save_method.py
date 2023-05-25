from abc import ABC, abstractmethod


class SaveMethod(ABC):
    @abstractmethod
    def save(self):
        ...

