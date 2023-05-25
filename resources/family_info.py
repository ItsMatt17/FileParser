import typing

class FamilyInfo:
    def __init__(self, save_method):
        self._parent : str | None = None
        self._parent_line_num: int | None = None
        self._children: list[str] = []
        self._current_file = None
        self._unique_child_found = False

        self.save_method = save_method

    def save_data(self, file_path) -> None:
        self.save_method(parent=self._parent, line_num=self._parent_line_num, children=self._children,
                                        file_path=file_path)

    def new_parent(self, new_parent : str, new_line_num : int, current_file : str):
        if self._unique_child_found:
            self.save_data(current_file)

        self._parent = new_parent
        self._parent_line_num = new_line_num
        self._children.clear()
        self._unique_child_found = False

    @property
    def unique_child_found(self):
        return self._unique_child_found

    @unique_child_found.setter
    def unique_child_found(self, value : bool):
        self._unique_child_found = value

    def add_child(self, child : str):
        self._children.append(child)

    def has_unique_child(self) -> bool:
        return self._unique_child_found

    @property
    def parent(self):
        return self._parent


