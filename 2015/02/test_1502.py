#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aoc_1502

with open('tests/test.txt') as input_file:
        input_data = input_file.read()

dimensions = aoc_1502.parse_input(input_data)
assert dimensions == [[2, 3, 4],
                 [1, 1, 10]]

assert [aoc_1502.wrapping_paper(sides) for sides in dimensions] == [58, 43]
assert [aoc_1502.ribbon(sides) for sides in dimensions] == [34, 14]
