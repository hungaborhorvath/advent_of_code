#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


def parse_input(input_data:str) -> tuple[list[list[int]], list[str]]:
    lines = [line for line in input_data.split('\n') if line]
    numbers = [[int(s) for s in line.split()] for line in lines[:-1]]
    operations = lines[-1].split()
    return numbers, operations

def parse_input_for_part_two(input_data:str) -> list[str]:
    lines = [line for line in input_data.split('\n') if line]
    return lines[:-1]


def length_of_columns(columns:list[int]) -> list[int]:
    return [max([len(str(n)) for n in column]) for column in columns]

def create_columns_for_second_part(number_lines:list[str],
                                   lengths:list[int]) -> list[int]:
    columns = []
    start = 0
    for length in lengths:
        end = start + length
        column_str = [number_line[start:end] for number_line in number_lines]
        column = [int(''.join(t)) for t in list(zip(*column_str))]
        columns.append(column)
        start = end+1
    return columns


def add(column:list[int]) -> int:
    return sum(column)

def multiply(column:list[int]) -> int:
    return math.prod(column)


def do_operations_on_numbers(columns:list[list[int]],
                             operations:list[str]) -> list[int]:
    results = []
    for i, column in enumerate(columns):
        if operations[i] == '+':
            results.append(add(column))
        elif operations[i] == '*':
            results.append(multiply(column))
    return results


def main(file_name:str) -> tuple[int, int]:
    with open(file_name) as input_file:
        input_data = input_file.read()
    numbers, operations = parse_input(input_data)
    number_lines = parse_input_for_part_two(input_data)
    columns = list(zip(*numbers))
    results_for_part_one = do_operations_on_numbers(columns, operations)
    lengths = length_of_columns(columns)
    columns_for_second_part = create_columns_for_second_part(number_lines,
                                                             lengths)
    results_for_part_two = do_operations_on_numbers(columns_for_second_part,
                                                    operations)
    answer = (sum(results_for_part_one), sum(results_for_part_two))
    return answer

if __name__ == '__main__':
    sys.exit(main(sys.argv[-1]))
