#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import itertools
import math

def parse_input(input_data: str) -> list[list[int]]:
    dimensions_str = input_data.split('\n')
    dimensions = [s.split('x') for s in dimensions_str if s]
    return [[int(s) for s in sides] for sides in dimensions]

def wrapping_paper(sides: list[int]) -> int:
    surface = sum(2*a*b for a, b in itertools.combinations(sides, 2))
    sorted_sides = sorted(sides)
    slack = sorted_sides[0]*sorted_sides[1]
    return surface + slack

def ribbon(sides: list[int]) -> int:
    sorted_sides = sorted(sides)
    present = 2*(sorted_sides[0]+sorted_sides[1])
    bow = math.prod(sides)
    return present + bow

def main(file_name: str) -> tuple[int, int]:
    with open(file_name) as input_file:
        input_data = input_file.read()
    dimensions = parse_input(input_data)
    answer = (sum(wrapping_paper(sides) for sides in dimensions),
              sum(ribbon(sides) for sides in dimensions))
    return answer

if __name__ == '__main__':
    sys.exit(main(sys.argv[-1]))

