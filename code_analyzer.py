#! usr/bin/env python
import re

FILEPATH = "source.txt"


def load_file(file_name: str):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def find_int_functions(file_str: str):
    pattern = r'int \w+\('
    regex = re.compile(pattern)
    function_names = [item[len('int') + 1:-1] for item in regex.findall(file_str)]
    print(function_names)


def main():
    file_str = load_file(FILEPATH)
    find_int_functions(file_str)


if __name__ == '__main__':
    main()
