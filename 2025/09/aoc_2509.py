#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import itertools


def parse_input(input_data:str) -> list[tuple[int, int]]:
    lines = [line for line in input_data.split('\n') if line]
    red_tiles = [tuple(int(s) for s in line.split(',')) for line in lines]
    return red_tiles


def rectangle(
        corners:tuple[tuple[int, int], tuple[int, int]]
        ) -> tuple[tuple[int, int], tuple[int, int],
                   tuple[int, int], tuple[int, int]]:
    (a, b) = corners[0]
    (c, d) = corners[1]
    (x, u) = (min(a, c), max(a, c))
    (y, v) = (min(b, d), max(b, d))
    return ((x, y), (x, v), (u, y), (u, v))

def area(corners:tuple[tuple[int, int], tuple[int, int]]) -> int:
    (a, b) = corners[0]
    (c, d) = corners[1]
    return (abs(a-c)+1)*(abs(b-d)+1)

def find_largest_rectangle_by_area(
        red_tiles:list[tuple[int, int]]
        ) -> tuple[tuple[int, int], tuple[int, int]]:
    red_tile_pairs = itertools.combinations(red_tiles, 2)
    ordered_by_area_red_tile_pairs = sorted(red_tile_pairs, key=area,
                                            reverse=True)
    return ordered_by_area_red_tile_pairs[0]


def borderline_intersects_with_inside_of_rectangle(
        corners:tuple[tuple[int, int], tuple[int, int]],
        red_tile1:tuple[int, int],
        red_tile2:tuple[int, int],
        ) -> bool:
    (x, y) = rectangle(corners)[0]
    (u, v) = rectangle(corners)[-1]
    ## either a == c or b == d
    (a, b) = rectangle((red_tile1, red_tile2))[0]
    (c, d) = rectangle((red_tile1, red_tile2))[-1]
    return a < u and c > x and b < v and d > y

def border_intersects_with_inside_of_rectangle(
        corners:tuple[tuple[int, int], tuple[int, int]],
        red_tiles:list[tuple[int, int]]
        ) -> bool:
    for i in range(len(red_tiles)):
        red_tile1 = red_tiles[i-1]
        red_tile2 = red_tiles[i]
        if borderline_intersects_with_inside_of_rectangle(corners,
                                                          red_tile1, red_tile2):
            return True
    return False

def is_green_rectangle(corners, red_tiles):
    return not border_intersects_with_inside_of_rectangle(corners, red_tiles)

def find_largest_green_rectangle_by_area(
        red_tiles:list[tuple[int, int]],
        ) -> tuple[tuple[int, int], tuple[int, int]]:
    red_tile_pairs = itertools.combinations(red_tiles, 2)
    ordered_by_area_red_tile_pairs = sorted(red_tile_pairs, key=area,
                                            reverse=True)
    for tile_pair in ordered_by_area_red_tile_pairs:
        if is_green_rectangle(tile_pair, red_tiles):
            break
    return tile_pair


def main(file_name:str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    red_tiles = parse_input(input_data)
    answer = (area(find_largest_rectangle_by_area(red_tiles)),
              area(find_largest_green_rectangle_by_area(red_tiles)))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
