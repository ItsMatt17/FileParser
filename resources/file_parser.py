import pathlib

from resources.ABCs.parse_strategy import ParseStrategy
from resources.Data.save_file_data import Storage
from resources.directory import Directory
class FileParser:
    def __init__(self, directory : Directory, strategy : ParseStrategy):
        #~~~~~~~~ Dependencies ~~~~~~~~~
        self.__directory : Directory = directory
        self.__save_method = Storage
        self.__strategy : ParseStrategy = strategy

    def iter_folders(self):
        PATH_TO_WALK = self.__directory.walk_path()

        file : pathlib.Path
        for file_count, file in enumerate(PATH_TO_WALK):
            print(f"Currently on file: {file_count + 1} | File Path: {self.__directory.current_file_path}")
            with file.open() as f:
                self.__strategy.parse(f, str(file.absolute()))

