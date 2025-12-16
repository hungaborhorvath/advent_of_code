#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import sys
import itertools
import math
import attrs
import networkx as nx


@attrs.define(frozen=True)
class Point():
    x:int = attrs.field()
    y:int = attrs.field()
    z:int = attrs.field()
    @classmethod
    def from_str(cls, s:str):
        return cls(*[int(coordinate) for coordinate in s.split(',')])
    def distance_square(self, other:Point) -> int:
        return ((self.x - other.x)**2 + (self.y - other.y)**2
                + (self.z - other.z)**2)

def distance_square_between_points(point_pair:tuple[Point, Point]) -> int:
    p, q = point_pair
    return p.distance_square(q)


def parse_input(input_data:str) -> list[Point]:
    points = [Point.from_str(line) for line in input_data.split('\n') if line]
    return points


def graph_from_points(points:list[Point],
                      number_of_edges:int) -> nx.Graph:
    G = nx.Graph() # type:nx.Graph
    G.add_nodes_from(points)
    point_pairs = list(itertools.combinations(points, 2))
    ordered_point_pairs = sorted(point_pairs,
                                 key=distance_square_between_points)
    G.add_edges_from(ordered_point_pairs[:number_of_edges])
    return G

def last_point_pair_for_connected_graph(
        points:list[Point]
        ) -> tuple[Point, Point]:
    G = nx.Graph() # type:nx.Graph
    G.add_nodes_from(points)
    point_pairs = list(itertools.combinations(points, 2))
    ordered_point_pairs = sorted(point_pairs,
                                 key=distance_square_between_points)
    i = -1
    while not nx.is_connected(G):
        i += 1
        G.add_edge(*ordered_point_pairs[i])
    return ordered_point_pairs[i]


def main(file_name:str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    points = parse_input(input_data)
    number_of_edges = 10 if len(points) == 20 else 1000
    G = graph_from_points(points, number_of_edges)
    components = list(nx.connected_components(G))
    ordered_components = sorted(components, key=len, reverse=True)
    (p, q) = last_point_pair_for_connected_graph(points)
    answer = (math.prod(len(c) for c in ordered_components[:3]), p.x * q.x)
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
