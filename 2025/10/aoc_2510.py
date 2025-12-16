#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from typing import cast, Optional, Union
from itertools import chain, combinations, product
from collections import Counter
import sympy


## https://docs.python.org/3/library/itertools.html
def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def parse_input(input_data:str) -> list[str]:
    lines = [line for line in input_data.split('\n') if line]
    return lines

def parse_lights(s:str) -> set[int]:
    lights = set([])
    for i, c in enumerate(s):
        if c == '#':
            lights.add(i)
    return lights

def parse_button(s:str) -> tuple[int, ...]:
    t = tuple(int(nr) for nr in s.split(','))
    return t

def parse_joltage(s:str) -> list[int]:
    l = [int(nr) for nr in s.split(',')]
    return l

def parse_atom(s:str) -> Optional[Union[set[int], tuple[int, ...], list[int]]]:
    parentheses = (s[0], s[-1])
    if parentheses == ('[', ']'):
        return parse_lights(s[1:-1])
    if parentheses == ('(', ')'):
        return parse_button(s[1:-1])
    if parentheses == ('{', '}'):
        return parse_joltage(s[1:-1])
    return None

def parse_line(line:str) -> tuple[set[int],
                                  tuple[tuple[int, ...], ...],
                                  list[int]]:
    l = [parse_atom(atom) for atom in line.split()]
    lights, all_buttons, joltage = l[0], l[1:-1], l[-1]
    ## these typings are actually based on assumption on the input
    lights_with_correct_type = cast(set[int], lights)
    all_buttons_with_correct_type = cast(tuple[tuple[int, ...], ...],
                                         all_buttons)
    joltage_with_correct_type = cast(list[int], joltage)
    return (lights_with_correct_type, all_buttons_with_correct_type,
            joltage_with_correct_type)


def press_buttons(buttons:list[tuple[int, ...]]):
    lights = Counter(sum([list(button) for button in buttons], []))
    return set(light for light, button_count in lights.items()
                     if button_count % 2)


def find_number_of_lowest_button_presses_for_lights(
        lights:set[int],
        all_buttons:tuple[tuple[int, ...], ...]
        ) -> int:
    for buttons in powerset(all_buttons):
        if press_buttons(buttons) == lights:
            return len(buttons)
    ## this should be infinity based on the spirit of the puzzle
    ## but we assume this is never reached for the input, anyway
    return 0


def buttons_having_index(
        i:int,
        buttons:tuple[tuple[int, ...], ...]
        ) -> list[tuple[int, ...]]:
    return [button for button in buttons if i in button]

def max_press_for_button(
        joltage:list[int],
        button:tuple[int, ...]
        ) -> int:
    return min(joltage[i] for i in button)

def matrix_for_buttons(
        joltage:list[int],
        all_buttons:tuple[tuple[int, ...], ...]
        ) -> list[list[int]]:
    matrix = []
    for button in all_buttons:
        row = []
        for i, _ in enumerate(joltage):
            if i in button:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def v(t:tuple) -> sympy.Symbol:
    return sympy.Symbol('v_' + str(t), integer=True)


def find_number_of_lowest_button_presses_for_joltage(
        joltage:list[int],
        all_buttons:tuple[tuple[int, ...], ...],
        use_heuristic=True,
        ) -> int:
    variables = [v(button)
                 for button in sorted(all_buttons, key=len, reverse=True)]
    expression = sum(variables)
    equations = []
    for i, jolt in enumerate(joltage):
        equations.append(
            sympy.Eq(sum(v(button)
                         for button in buttons_having_index(i, all_buttons)),
                     jolt)
            )
    sols = sympy.solve(equations, variables, dict=True)
    ## this should be guaranteed by sympy.solve....
    assert len(sols) == 1
    sol = sols[0]
    free_variables = tuple(sympy.Tuple(*tuple(sol.values())).atoms(*variables))

    bounds = {v(button): max_press_for_button(joltage, button)
              for button in all_buttons}
    l = list(product(*[range(bounds[variable])
                       for variable in free_variables]))

    new_expression = cast(sympy.Expr, expression).xreplace(sol)
    def expression_for_value(values:tuple[int, ...]) -> bool:
        subs = {variable: values[i]
                for i, variable in enumerate(free_variables)}
        return new_expression.xreplace(subs)
    new_l = sorted(l, key=expression_for_value) if use_heuristic else l

    all_valid_solutions = []
    for values in new_l:
        subs = {variable: values[i]
                for i, variable in enumerate(free_variables)}
        new_sol = {variable: solution.xreplace(subs)
                   for variable, solution in sol.items()}
        new_sol.update(subs)
        if all(isinstance(value, (sympy.Integer, int)) and value >= 0
               for value in new_sol.values()):
            all_valid_solutions.append(new_sol)
            if use_heuristic:
                break
    return min(sum(solution.values()) for solution in all_valid_solutions)


def main(file_name:str) -> tuple[int, int]:
    with open(file_name, encoding="utf-8") as input_file:
        input_data = input_file.read()
    lines = parse_input(input_data)
    machines = [parse_line(line) for line in lines]
    lowest_number_of_presses_for_lights = [
        find_number_of_lowest_button_presses_for_lights(machine[0], machine[1])
        for machine in machines
        ]
    lowest_number_of_presses_for_joltage = [
        find_number_of_lowest_button_presses_for_joltage(machine[2],
                                                         machine[1])
        for machine in machines
        ]
    answer = (sum(lowest_number_of_presses_for_lights),
              sum(lowest_number_of_presses_for_joltage))
    return answer

if __name__ == '__main__':
    print(main(sys.argv[-1]))
