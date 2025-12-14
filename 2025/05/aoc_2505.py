#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def parse_input(input_data:str) -> tuple[list[tuple[int, int]], list[int]]:
    [intervals_str, ids_str] = input_data.split('\n\n')
    intervals = [line.split('-') for line in intervals_str.split('\n') if line]
    intervals_int = [(int(a), int(b)) for (a, b) in intervals]
    ids_int = [int(line) for line in ids_str.split('\n') if line]
    return (intervals_int, ids_int)


def is_fresh_id(id:int, intervals:list[tuple[int, int]]) -> bool:
    fresh = False
    for (a, b) in intervals:
        if a <= id and id <= b:
            fresh = True
            break
    return fresh


def all_fresh_ids_slow(intervals:list[tuple[int, int]]) -> set[int]:
    ## way too inefficient
    fresh_ids = set([])
    for (a, b) in intervals:
        for i in range(a, b+1):
            fresh_ids.add(i)
    return fresh_ids


def have_intersection_with(interval:tuple[int, int],
                           intervals:set[tuple[int, int]]) -> list[tuple[int, int]]:
    (x, y) = interval
    has_intersection = set([])
    for (a, b) in intervals:
        if not (y < a or x > b):
            has_intersection.add((a, b))
    return list(has_intersection)

def add_new_interval(interval:tuple[int, int],
                     disjoint_intervals:set[tuple[int, int]]):
    (x, y) = interval
    has_intersection = have_intersection_with((x, y), disjoint_intervals)
    if has_intersection:
        new_disjoint_intervals = disjoint_intervals.copy()
        for interval in has_intersection:
            new_disjoint_intervals.remove(interval)
        has_intersection.append((x, y))
        start = min(interval[0] for interval in has_intersection)
        end = max(interval[1] for interval in has_intersection)
        new_disjoint_intervals.add((start, end))
    else:
        new_disjoint_intervals = disjoint_intervals.union(set([(x, y)]))
    return new_disjoint_intervals

def all_disjoint_intervals(intervals:list[tuple[int, int]]) -> set[tuple[int, int]]:
    all_intervals = set([]) # type:set[tuple[int, int]]
    for interval in intervals:
        all_intervals = add_new_interval(interval, all_intervals)
    return all_intervals

def number_of_all_fresh_ids(disjoint_intervals:set[tuple[int, int]]) -> int:
    s = 0
    for (a, b) in disjoint_intervals:
        s += b + 1
        s -= a
    return s


def main(file_name:str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    intervals, ids = parse_input(input_data)
    fresh_ids = [id for id in ids if is_fresh_id(id, intervals)]
    answer = (len(fresh_ids),
              number_of_all_fresh_ids(all_disjoint_intervals(intervals)))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
