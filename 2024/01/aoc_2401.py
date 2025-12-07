#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def parse_input(input_data: str) -> list[list[int]]:
    l = [[], []] # type:list[list[int]]
    merged_numbers = input_data.split()
    for i, nr in enumerate(merged_numbers):
        l[i%2].append(int(nr))
    return l

def differences(l1: list[int], l2: list[int]) -> list[int]:
    l = []
    for a, b in zip(sorted(l1), sorted(l2)):
        l.append(abs(a-b))
    return l

def similarity_score(l1: list[int], l2: list[int]) -> int:
    return sum(a*l2.count(a) for a in l1)

def main(file_name: str):
    with open(file_name) as input_file:
        input_data = input_file.read()
    l1, l2 = parse_input(input_data)
    answer = (sum(differences(l1, l2)), similarity_score(l1, l2))
    return answer

if __name__ == '__main__':
    sys.exit(main(sys.argv[-1]))

