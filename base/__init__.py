import os
path = os.path.abspath(os.path.dirname(__file__))
print(path)
print(os.sep)
list_path = path.split(os.sep)
list_path = list_path[:len(list_path) - 1:]
print(list_path)
base_path=""
for i in list_path:
    base_path += i+os.sep
BASE_PATH = base_path
print(BASE_PATH)


