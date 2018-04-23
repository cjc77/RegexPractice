#! usr/bin/env python3
import re


def find_all_or(pattern, string):
    regex = re.compile(pattern, re.IGNORECASE)
    res = regex.findall(string)
    print(res)


def find_all_start(pattern, string):
    print(re.findall(pattern, string, re.MULTILINE))


def find_all_end(pattern, string):
    print(re.findall(pattern, string, re.MULTILINE))


def load_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def main():
    pattern1 = r'cats|dogs'
    string1 = "Cats and dogs, cats"
    pattern2 = r"^\w+"
    string2 = (
        "This string"
        "\ntakes more than"
        "\none line"
    )
    pattern3 = r".+\)$"
    string3 = load_file("source.txt")
    find_all_or(pattern1, string1)
    find_all_start(pattern2, string2)
    find_all_end(pattern3, string3)


if __name__ == '__main__':
    main()
