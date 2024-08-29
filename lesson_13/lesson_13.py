from pathlib import Path

desired_file_path: Path = Path('/Users/dart_brovsky/PycharmProjects/aqa_python_hillel/')
lesson_13_path: Path = desired_file_path / 'lesson_13'

# included_directories: list = [directory for directory in desired_file_path.iterdir() if directory.is_dir()]
# included_file: list = [file for file in desired_file_path.iterdir() if file.is_file()]

extension = '.txt'
files_with_extension = [file for file in lesson_13_path.iterdir() if file.suffix == extension]

for file in files_with_extension:
    print(file)
    print(file.name)
    print(file.suffix)

# for directory in included_directories:
#     print(directory)

# for file in included_file:
#     print(file)

# print(files_with_extension)
# print(desired_file_path.exists())

print(Path.home())
print(Path.cwd())

windows_path = "C:\\Users\\Username"

print(windows_path)


# Вказуємо шлях до нової директорії
# new_directory: Path = lesson_13_path / 'dir/dir_sub3'
# # Створюємо нову директорію
# new_directory.mkdir(parents=True, exist_ok=False)
#
# with open('/Users/dart_brovsky/PycharmProjects/aqa_python_hillel/lesson_13/test_data.txt', 'r') as file:
#     print(file.read())
#
# with open('/Users/dart_brovsky/PycharmProjects/aqa_python_hillel/lesson_13/test_data_file.txt', 'r') as file:
#     print(file.write("New file"))

import json

with open('test_date.json', 'r') as file:
    data = json.load(file)


print(data)

json_object: str = '{"data": "Serhii", "number": 20}'

data = json.loads(json_object)
print(data)

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

json_string = json.dumps(data, indent=4)

# print(json_string)

import xml.etree.ElementTree as ET

tree = ET.parse('test_data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.text)
