#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


START = 50
DIAL_SIZE = 100


class WrongInputError(Exception):
    pass


def parse_input(input_data: str) -> list[int]:
    numbers = []
    rotations = input_data.split()
    for nr in rotations:
        if nr[0] == 'L':
            numbers.append(-int(nr[1:]))
        elif nr[0] == 'R':
            numbers.append(int(nr[1:]))
        else:
            raise WrongInputError(nr)
    return numbers

def dial_states(numbers:list[int], start:int =START,
                                   dial_size:int =DIAL_SIZE) -> list[int]:
    dial = start
    dial_sequence = [dial]
    for n in numbers:
        dial = (dial + n) % dial_size
        dial_sequence.append(dial)
    return dial_sequence

def number_of_zeros(numbers:list[int], start:int =START,
                                       dial_size:int =DIAL_SIZE) -> int:
    dial = start
    count_of_zeros = 0
    for n in numbers:
        new_dial = dial + n
        hundreds = new_dial // dial_size
        count_of_zeros += abs(hundreds)
        if new_dial <= 0:
            ## if we started from 0 and went negative, then we overcounted by 1
            if dial == 0:
                count_of_zeros -= 1
            ## if we arrive at 0 by going negative, then we undercounted by 1
            elif new_dial % dial_size == 0:
                count_of_zeros += 1
        dial = new_dial % dial_size
    return count_of_zeros


def main(file_name: str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    numbers = parse_input(input_data)
    dial_sequence = dial_states(numbers)
    answer = (dial_sequence.count(0), number_of_zeros(numbers))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
