#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def parse_input(input_data:str) -> list[list[bool]]:
    lines = [line for line in input_data.split('\n') if line]
    rolls = [[s == '@' for s in line] for line in lines]
    return rolls


def accessible_roll(rolls:list[list[bool]],
                    coords:tuple[int, int],
                    max_coords:tuple[int, int],
                    min_coords:tuple[int, int] =(0, 0)) -> bool:
    i, j = coords
    maxi, maxj = max_coords
    mini, minj = min_coords
    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1),
                  (i+1, j-1), (i+1, j), (i+1, j+1)]
    valid_neighbors = [(k, l) for (k, l) in neighbors
                       if (mini <= k < maxi)
                       and (minj <= l < maxj)]
    valid_neighbor_rolls = [(k, l) for (k, l) in valid_neighbors
                            if rolls[k][l]]
    return rolls[i][j] and len(valid_neighbor_rolls) < 4

def accessible_rolls(rolls) -> list[tuple[int, int]]:
    maxi = len(rolls)
    maxj = len(rolls[0])
    l = []
    for i in range(maxi):
        for j in range(maxj):
            if accessible_roll(rolls, (i, j), (maxi, maxj)):
                l.append((i, j))
    return l


def rolls_after_remove(rolls:list[list[bool]],
                       removeables:list[tuple[int, int]]) -> list[list[bool]]:
    new_rolls = rolls.copy()
    for (i, j) in removeables:
        new_rolls[i][j] = False
    return new_rolls

def number_of_removeable_rolls(rolls:list[list[bool]]) -> int:
    s = 0
    new_rolls = rolls.copy()
    while accessible_rolls(new_rolls):
        s += len(accessible_rolls(new_rolls))
        new_rolls = rolls_after_remove(new_rolls, accessible_rolls(new_rolls))
    return s


def main(file_name:str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    rolls = parse_input(input_data)
    answer = (len(accessible_rolls(rolls)), number_of_removeable_rolls(rolls))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
