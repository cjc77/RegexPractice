#! usr/bin/env python3
import re

FILEPATH = "source.txt"


def load_file(file_name: str):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def print_function_arguments(code_str: str):
    fun_args = re.compile(r"""print\(.*\)""")
    res = [item.lstrip(' ').lstrip('"').rstrip('"')
           for mtch in fun_args.findall(code_str)
           for item in mtch[len("print") + 1:-1].split(',')]
    print(res)


def main():
    file_str = load_file(FILEPATH)
    print_function_arguments(file_str)


if __name__ == '__main__':
    main()
