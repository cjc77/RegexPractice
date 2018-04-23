#! usr/bin/env python3
import re


def results(regex, string):
    res = regex.findall(string)
    print(res)


def main():
    string1 = "This is a test to -22 see if the the regex 54 object can find all numbers in 7 this string."
    pattern1 = r'\d+'
    pattern2 = r'\s+\w+|\w+'
    regex1 = re.compile(pattern1)
    regex2 = re.compile(pattern2)
    results(regex1, string1)
    results(regex2, string1)


if __name__ == '__main__':
    main()
