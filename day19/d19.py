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
        self.op = None
        if self.R or self.A:
            return
        parts = rule.split(':')
        if len(parts) == 2:
            part, op, val = parse.parse('{:w}{:1}{:d}', parts.pop(0)).fixed
            self.op = (part, op, val)
        if parts[0] == 'A': self.A = True
        elif parts[0] == 'R': self.R = True
        else: self.next = parts[0]

    def __str__(self):
        return f'A={self.A}, R={self.R}, next={self.next}'

    def validate(self, part):
        return self.op == None or (self.op[1] == '>' and part[self.op[0]] > self.op[2]) or (self.op[1] == '<' and part[self.op[0]] < self.op[2])

    def process(self, part):
        if self.validate(part) == True:
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

    def accepted(self, part):
        w = 'in'
        while w not in ['R', 'A']:
            w = self.workflows[w].process(part)
        return w == 'A'

    def solve(self):
        return sum([sum(part.values()) for part in self.parts if self.accepted(part)])

    def solve2(self):
        c = defaultdict(lambda: set([1,4001]))
        for w in self.workflows.values():
            for r in w.rules:
                if not r.op:
                    continue
                c[r.op[0]].add(r.op[2] + (0 if r.op[1] == '<' else 1))
        ss = 0
        for t in 'xmas':

            c[t] = sorted(list(c[t]))

        print(len(c['x'])*len(c['m'])*len(c['a'])*len(c['s']))
        for x in range(len(c['x'])-1):
            for m in range(len(c['m'])-1):
                print(c['x'][x], c['m'][m])
                for a in range(len(c['a'])-1):
                    for s in range(len(c['s'])-1):
                        if self.accepted({'x':c['x'][x], 'm':c['m'][m], 'a':c['a'][a], 's': c['s'][s]}):
                            ss += (c['x'][x+1] - c['x'][x])*(c['m'][m+1] - c['m'][m])*(c['a'][a+1] - c['a'][a])*(c['s'][s+1] - c['s'][s])
        return ss


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
