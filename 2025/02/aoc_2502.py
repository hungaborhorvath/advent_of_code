#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def parse_input(input_data: str) -> list[tuple[int, ...]]:
    ranges = []
    for range_string in input_data.split(','):
        ranges.append(tuple(int(n) for n in range_string.split('-')))
    return ranges


def is_invalid_id(n: int, d:int =2) -> bool:
    s = str(n)
    length = len(s)
    if length % d != 0:
        return False
    pattern_length = length // d
    return len(set(s[i*pattern_length:(i+1)*pattern_length]
                   for i in range(d))) == 1


def invalid_ids_in_range(start:int, end:int) -> list[int]:
    invalid_ids = []
    ## naive approach to iterate through all ids
    ## slow, but manageable
    for n in range(start, end+1):
        if is_invalid_id(n):
            invalid_ids.append(n)
    return invalid_ids

def all_invalid_ids_in_range(start:int, end:int) -> list[int]:
    invalid_ids = []
    ## naive approach to iterate through all ids and potential pattern lengths
    ## quite slow, but still manageable
    for n in range(start, end+1):
        for d in range(2, len(str(n)) + 1):
            if is_invalid_id(n, d):
                invalid_ids.append(n)
                break
    return invalid_ids


def invalid_ids_in_input(ranges:list) -> list[int]:
    invalid_ids = [invalid_ids_in_range(start, end) for (start, end) in ranges]
    return sum(invalid_ids, start=[])

def all_invalid_ids_in_input(ranges:list) -> list[int]:
    all_invalid_ids = [all_invalid_ids_in_range(start, end)
                       for (start, end) in ranges]
    return sum(all_invalid_ids, start=[])


def main(file_name: str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    ranges = parse_input(input_data)
    invalid_ids = invalid_ids_in_input(ranges)
    all_invalid_ids = all_invalid_ids_in_input(ranges)
    answer = (sum(invalid_ids), sum(all_invalid_ids))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
