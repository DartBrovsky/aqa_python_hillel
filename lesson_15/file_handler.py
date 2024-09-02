from typing import IO, TextIO


class FileHandler:

    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode

        self.file: TextIO = open(self.file_name, self.mode)
        print("File was opened successfully")

    def read_data_from_file(self) -> str:
        return self.file.read()

    def __del__(self) -> None:
        self.file.close()
        print("File was closed successfully.")


file_handler: FileHandler = FileHandler("my_text.txt", "r")

print(file_handler.read_data_from_file())

del file_handler
