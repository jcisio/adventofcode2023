"""
Advent Of Code
--- Day 12: Hot Springs ---
https://adventofcode.com/2023/day/12
"""
from __future__ import annotations
import re


class Problem:
    def __init__(self, input) -> None:
        self.input = input
        self.cached = {}

    def is_ok(self, parts, groups):
        new_list = list(map(len, re.sub(r'\.+', '.', parts.strip('.')).split('.')))
        return (new_list == groups) or (new_list == [0] and groups == [])

    def is_ok_partially(self, parts, groups):
        my_list = list(map(len, re.sub(r'\.+', '.', parts.strip('.')).split('.')))
        return len(my_list) <= len(groups) and my_list[0:-1] == groups[0:len(my_list)-1] and my_list[-1] <= groups[len(my_list)-1]

    def count_possible(self, parts, groups):
        key = parts + ':' + ','.join(map(str, groups))
        if key in self.cached:
            return self.cached[key]

        s = None
        i = parts.find('?')
        if i == -1:
            s = 1 if self.is_ok(parts, groups) else 0
        elif (len(groups) == 0 or groups[0] == 0) and parts.find('#') == -1:
            s = 1
        else:
            pre = list(map(len, re.sub(r'\.+', '.', parts[0:i].strip('.')).split('.')))
            if len(pre) > len(groups) or pre[0:-1] != groups[0:len(pre)-1] or pre[-1] > groups[len(pre)-1]:
                s = 0

        if s is not None:
            self.cached[key] = s
            return s

        s = 0

        # Replace with # if possible
        if (i > 0 and parts[i-1] == '.' and (pre[-1] == 0 or pre[-1] == groups[len(pre)-1])) or i == 0:
            new_parts = '#' + parts[i+1:]
            new_groups = groups[len(pre) if pre[-1] > 0 else 0:]
            s += self.count_possible(new_parts, new_groups)
        elif parts[i-1] == '#' and pre[-1] < groups[len(pre)-1]:
            new_parts = '#'*(pre[-1]+1) + parts[i+1:]
            new_groups = groups[len(pre)-1:]
            s += self.count_possible(new_parts, new_groups)

        # Replace with . if possible
        if pre[-1] == groups[len(pre)-1] or pre[-1] == 0:
            new_parts = parts[i+1:]
            new_groups = groups[len(pre) if pre[-1]>0 else 0:]
            s += self.count_possible(new_parts, new_groups)

        self.cached[key] = s
        return s

    def solve(self, r=1):
        return sum([self.count_possible(((parts+'?')*r)[0:-1], groups*r) for parts, groups in self.input])

    def solve2(self):
        return self.solve(5)


class Solver:
    def __init__(self, input) -> None:
        rows = []
        for row in input:
            parts, groups = row.split()
            rows.append((parts, list(map(int, groups.split(',')))))
        self.input = rows

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
