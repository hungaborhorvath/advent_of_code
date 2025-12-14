#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import functools
import math
import attrs


@attrs.define()
class Shape:
    index: int = attrs.field()
    shape: str = attrs.field()
    @functools.cached_property
    def coordinates(self) -> tuple[tuple[int, int], ...]:
        lines = self.shape.split('\n')
        return tuple((i, j)
                     for i, line in enumerate(lines)
                     for j, s in enumerate(line)
                     if s == '#')
    def __len__(self) -> int:
        return len(self.coordinates)

@attrs.define()
class Region:
    size: tuple[int, ...] = attrs.field()
    shapes_required: tuple[int, ...] = attrs.field()
    def __len__(self) -> int:
        return math.prod(self.size)
    def required_minimal_size(self, shapes:list[Shape]) -> int:
        return sum(required*len(shape)
                   for required, shape in zip(self.shapes_required, shapes))
    def impossible_to_fit_by_size(self, shapes:list[Shape]) -> bool:
        return len(self) < self.required_minimal_size(shapes)

def parse_region(size_shapes:str) -> Region:
    sizes, shapes = size_shapes.split(':')
    size = tuple(int(a) for a in sizes.split('x'))
    shapes_required = tuple(int(a) for a in shapes.split() if a)
    return Region(size, shapes_required)

def parse_input(input_data:str) -> tuple[list[Shape], list[Region]]:
    parts = [part for part in input_data.split('\n\n') if part]
    shapes = tuple(pc.split(':\n')[-1] for pc in parts[:-1])
    regions = [region for region in parts[-1].split('\n') if region]
    return ([Shape(i, shape) for i, shape in enumerate(shapes)],
            [parse_region(region) for region in regions])


def main(file_name:str) -> tuple[int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    shapes, regions = parse_input(input_data)
    ## exclude regions which are trivially impossible to fit by size
    ## and hope for the best.... :-)
    answer = (len([region for region in regions
                   if not region.impossible_to_fit_by_size(shapes)]),)
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
