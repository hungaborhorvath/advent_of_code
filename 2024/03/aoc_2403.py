#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import ast
import math

def parse_input(input_data:str) -> list[str]:
    lines = [line for line in input_data.split('\n') if line]
    return lines


def find_muls(line:str) -> list[str]:
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)

def find_muls_and_dos_and_donts(line:str) -> list[str]:
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)

def muls_while_do(muls:list[str]) -> list[str]:
    multiply = True
    muls_to_multiply = []
    for mul in muls:
        if mul == r"do()":
            multiply = True
        elif mul == r"don't()":
            multiply = False
        elif multiply:
            muls_to_multiply.append(mul)
    return muls_to_multiply

def convert_mul_to_integers(mul:str) -> tuple[int, int]:
    return ast.literal_eval(mul[3:])


def main(file_name: str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    lines = parse_input(input_data)
    muls = sum([find_muls(line) for line in lines], []) # type: list[str]
    muls_and_dos_and_donts = sum([find_muls_and_dos_and_donts(line)
                                  for line in lines], []) # type: list[str]
    muls_to_multiply = muls_while_do(muls_and_dos_and_donts)
    answer = (sum(math.prod(convert_mul_to_integers(mul)) for mul in muls),
              sum(math.prod(convert_mul_to_integers(mul))
                  for mul in muls_to_multiply),)
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
