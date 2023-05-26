
from resources.Data.save_file_data import Storage, Storage


class FamilyInfo:
    def __init__(self, save_class):
        self._parent : str | None = None
        self._parent_line_num: int | None = None
        self._children: list[str] = []
        self._current_file : str  | None = None
        self._unique_child_found : bool = False

        self.__save_class = save_class

    def save_data(self, file_path) -> None:
        self.__save_class(parent=self._parent, line_num=self._parent_line_num, children=self._children.copy(),
                                        file_path=file_path)


    def save_check(self, current_file : str):
        if self._unique_child_found:
            self.save_data(current_file)

    def new_parent(self, new_parent : str, new_line_num : int, current_file : str):
        self.save_check(current_file)

        self._children.clear()
        self._parent = new_parent
        self._parent_line_num = new_line_num
        self._unique_child_found = False

    def found_unique_child(self):
        self._unique_child_found = True

    def add_child(self, child : str):
        print(child)
        self._children.append(child)

    def has_unique_child(self) -> bool:
        return self._unique_child_found

    @property
    def parent(self):
        return self._parent


