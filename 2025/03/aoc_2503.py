#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def parse_input(input_data:str) -> list[str]:
    return [s for s in input_data.split('\n') if s]

def parse_bank(bank:str) -> list[int]:
    return [int(s) for s in bank]


def max_k_digit_number_in_bank(bank:list[int], digits:int =2) -> int:
    numbers = []
    ix = 0
    for i in range(digits):
        if i < digits - 1:
            sub_number = bank[ix:(i-digits+1)]
        else:
            sub_number = bank[ix:]
        k = max(sub_number)
        ix += sub_number.index(k) + 1
        numbers.append(k)
    return int(''.join([str(k) for k in numbers]))


def main(file_name:str):
    with open(file_name) as input_file:
        input_data = input_file.read()
    banks = parse_input(input_data)
    joltages = [
        [max_k_digit_number_in_bank(parse_bank(bank), 2) for bank in banks],
        [max_k_digit_number_in_bank(parse_bank(bank), 12) for bank in banks]
        ]
    answer = (sum(joltages[0]), sum(joltages[1]))
    return answer

if __name__ == '__main__':
    sys.exit(main(sys.argv[-1]))
