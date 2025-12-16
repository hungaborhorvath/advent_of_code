#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import Counter


def parse_input(input_data:str) -> list[str]:
    lines = [line for line in input_data.split('\n') if line]
    return lines


def compute_beam_timelines_and_splits(
        lines:list[str]
        ) -> tuple[Counter[int], int]:
    start = lines[0].index('S')
    beam_indices = [Counter({start:1})]
    splits = 0
    ## start line is already handled
    for line in lines[1:]:
        new_beam_indices = Counter({}) # type:Counter[int]
        for beam_index in beam_indices[-1].keys():
            if line[beam_index] == '.':
                new_beam_indices[beam_index] += beam_indices[-1][beam_index]
            elif line[beam_index] == '^':
                new_beam_indices[beam_index-1] += beam_indices[-1][beam_index]
                new_beam_indices[beam_index+1] += beam_indices[-1][beam_index]
                splits += 1
        beam_indices.append(new_beam_indices)
    return beam_indices[-1], splits


def main(file_name:str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    lines = parse_input(input_data)
    timelines, splits = compute_beam_timelines_and_splits(lines)
    answer = (splits, sum(timelines.values()))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
