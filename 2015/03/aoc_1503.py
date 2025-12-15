#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def parse_input(input_data:str) -> list[str]:
    lines = [line for line in input_data.split('\n') if line]
    return lines

def move(location:tuple[int, int], s:str) -> tuple[int, int]:
    new_location = list(location)
    if s == '^':
        new_location[1] += 1
    elif s == 'v':
        new_location[1] -= 1
    elif s == '>':
        new_location[0] += 1
    elif s == '<':
        new_location[0] -= 1
    return new_location[0], new_location[1]

def visited_houses(line:str,
                   start:tuple[int, int] =(0, 0),
                   step=1) -> list[tuple[int, int]]:
    visited = [start]
    for i, s in enumerate(line):
        if not i % step:
            visited.append(move(visited[-1], s))
    return visited


def main(file_name: str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    lines = parse_input(input_data)
    assert len(lines) == 1
    line = lines[0]
    movements = visited_houses(line)
    santa_next_year = visited_houses(line, step=2)
    robo_santa_next_year = visited_houses(line[1:], step=2)
    answer = (len(set(movements)),
              len(set(santa_next_year).union(set(robo_santa_next_year))))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
