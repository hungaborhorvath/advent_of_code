#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def parse_input(input_data: str) -> list[list[int]]:
    report_strs = input_data.split('\n')
    reports = [s.split(' ') for s in report_strs if s]
    return [[int(s) for s in report] for report in reports]

def is_safe(report: list[int]) -> bool:
    if not (sorted(report) == report or sorted(report, reverse=True) == report):
        return False
    safe = True
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]
    return set(differences).issubset(set([-3, -2, -1, 1, 2, 3]))

def is_safe_by_removing_one_element(report: list[int]) -> bool:
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

def main(file_name: str) -> tuple[int, int]:
    with open(file_name) as input_file:
        input_data = input_file.read()
    reports = parse_input(input_data)
    reports_is_safe = [is_safe(report) for report in reports]
    reports_is_safe_by_removing_one_element = [
        is_safe_by_removing_one_element(report) for report in reports
        ]
    answer = (reports_is_safe.count(True),
              reports_is_safe_by_removing_one_element.count(True))
    return answer

if __name__ == '__main__':
    sys.exit(main(sys.argv[-1]))

