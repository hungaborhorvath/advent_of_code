#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aoc_2402

with open('tests/test.txt') as input_file:
        input_data = input_file.read()

reports = aoc_2402.parse_input(input_data)
assert reports == [[7, 6, 4, 2, 1],
                   [1, 2, 7, 8, 9],
                   [9, 7, 6, 2, 1],
                   [1, 3, 2, 4, 5],
                   [8, 6, 4, 4, 1],
                   [1, 3, 6, 7, 9]]
assert [aoc_2402.is_safe(report) for report in reports] == [True,
                                                            False,
                                                            False,
                                                            False,
                                                            False,
                                                            True]

assert [aoc_2402.is_safe_by_removing_one_element(report)
        for report in reports] == [True,
                                   False,
                                   False,
                                   True,
                                   True,
                                   True]
