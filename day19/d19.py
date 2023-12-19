"""
Advent Of Code
--- Day 19: Aplenty ---
https://adventofcode.com/2023/day/19
"""
from __future__ import annotations
from collections import defaultdict
import parse
import re


class Rule:
    def __init__(self, rule):
        self.R = True if rule == 'R' else False
        self.A = True if rule == 'A' else False
        self.next = None
        self.condition = lambda _: True
        if self.R or self.A:
            return
        parts = rule.split(':')
        if len(parts) == 2:
            part, op, val = parse.parse('{:w}{:1}{:d}', parts.pop(0)).fixed
            self.condition = lambda x: (op == '>' and x[part] > val) or (op == '<' and x[part] < val)
        if parts[0] == 'A': self.A = True
        elif parts[0] == 'R': self.R = True
        else: self.next = parts[0]

    def __str__(self):
        return f'A={self.A}, R={self.R}, next={self.next}'

    def process(self, part):
        if self.condition(part) == True:
            return 'R' if self.R else 'A' if self.A else self.next
        return False

class Workflow:
    def __init__(self, rules):
        self.rules = rules

    def process(self, part):
        for rule in self.rules:
            #print(rule)
            r = rule.process(part)
            if r != False:
                break
        return r

class Problem:
    def __init__(self, input) -> None:
        workflows = {}
        for i, line in enumerate(input):
            if line == '':
                break
            name, rules = parse.parse('{:w}{}', line).fixed
            rules = list(map(Rule, rules[1:-1].split(',')))
            workflows[name] = Workflow(rules)

        parts = []
        for line in input[i+1:]:
            parts.append(dict(map(lambda p: parse.parse('{}={:d}', p), line[1:-1].split(','))))
        self.workflows = workflows
        self.parts = parts

    def solve(self):
        s = 0
        for part in self.parts:
            w = 'in'
            while w not in ['R', 'A']:
                w = self.workflows[w].process(part)
            if w == 'A':
                s += sum(part.values())
        return s

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
