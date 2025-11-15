#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def floor_counter(input_data: str) -> tuple[int, int]:
    s = 0
    counter = 0
    pos = 0
    for c in input_data:
        counter += 1
        if c == '(':
            s += 1
        elif c== ')':
            s -= 1
        if not pos and s == -1:
            pos = counter
    return (s, pos)

def main(file_name: str) -> tuple[int, int]:
    with open(file_name) as input_file:
        input_data = input_file.read()
    answer = floor_counter(input_data)
    return answer

if __name__ == '__main__':
    sys.exit(main(sys.argv[-1]))

