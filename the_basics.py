#! usr/bin/env python3

import re


def match_start(string, regex):
    match = regex.match(string)
    print(match.group(), match.start(), match.end(), match.span())


def match_first(string, regex):
    match = regex.search(string)
    print(match.group(), match.span())


def match_list(string, regex):
    match = regex.findall(string)
    for i in range(len(match)):
        print("{0}, Start Index: {1}".format(match[i], (len(match[i])) * i))


def match_iter(string, regex):
    match = regex.finditer(string)
    counter = 0
    for m in match:
        print(m.group(), "Start Index: {}".format(len(str(m.group())) * counter))
        counter += 1


def call_match_function(f_ptr, string: str, regex):
    f_ptr(string, regex)


def perform_all_matchings(table: list, string: str, regex):
    for f_ptr in table:
        call_match_function(f_ptr, string, regex)


fdt = [
    match_start,
    match_first,
    match_list,
    match_iter,
]


def main():
    string1 = 'abab'
    pattern_ab = r'ab*'
    regex1 = re.compile(pattern_ab)
    perform_all_matchings(fdt, string1, regex1)


if __name__ == '__main__':
    main()
