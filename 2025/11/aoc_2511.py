#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import functools
import itertools
import math
import networkx as nx


def parse_input(input_data:str) -> list[str]:
    lines = [line for line in input_data.split('\n') if line]
    return lines

def parse_line(line:str) -> tuple[str, list[str]]:
    l = line.split(':')
    start = l[0]
    ends = l[1].split()
    return (start, ends)

def input_graph(lines:list[str]) -> nx.DiGraph:
    dg = nx.DiGraph()
    for line in lines:
        start, ends = parse_line(line)
        edges = [(start, end) for end in ends]
        dg.add_edges_from(edges)
    return dg


@functools.cache
def number_of_path_between(dg:nx.DiGraph, start:str, end:str) -> int:
    if start == end:
        return 1
    else:
        return sum(number_of_path_between(dg, start, v)
                   for v in dg.predecessors(end))


def path_can_be_fulfilled(dg:nx.DiGraph, path:list[str]) -> bool:
    return all(path[i+1] in nx.descendants(dg, path[i])
               for i in range(len(path)-1))

def component_between(dg:nx.DiGraph, start:str, end:str) -> nx.DiGraph:
    nodes = [node for node in dg.nodes() if node in nx.descendants(dg, start)
                                         and end in nx.descendants(dg, node)]
    nodes.append(start)
    nodes.append(end)
    return nx.subgraph(dg, nodes)

def number_of_all_valid_path(dg:nx.DiGraph, start:str, end:str,
                   other_nodes:list[str]) -> int:
    s = 0
    for nodes in itertools.permutations(other_nodes):
        path = list(nodes)
        path.insert(0, start)
        path.append(end)
        if path_can_be_fulfilled(dg, path):
            s += math.prod([
                number_of_path_between(
                    component_between(dg, path[i], path[i+1]),
                    path[i],
                    path[i+1]
                    )
                for i in range(len(path)-1)
                ])
    return s


def main(file_name:str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    lines = parse_input(input_data)
    dg = input_graph(lines)
    answer = (number_of_path_between(dg, 'you', 'out'),
              number_of_all_valid_path(dg, 'svr', 'out', ['dac', 'fft']))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
