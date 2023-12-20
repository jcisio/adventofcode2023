"""
Advent Of Code
--- Day 20: Pulse Propagation ---
https://adventofcode.com/2023/day/20
"""
from __future__ import annotations
from collections import defaultdict
import math


class Problem:
    def __init__(self, input) -> None:
        modules = {}
        # low = off = False
        names = set()
        for line in input:
            m, o = line.split(' -> ')
            if m == 'broadcaster':
                m = 'B' + m
            module = {
                'name': m[1:],
                'type': m[0],
                'state': False,
                'output': o.split(', '),
                'input': {}
            }
            names = names.union(module['output'])
            modules[module['name']] = module
        for name in names:
            if name not in modules:
                modules[name] = {
                    'name': name,
                    'type': 'O',
                    'state': False,
                    'output': [],
                    'input': {}
                }
        for m in modules:
            for o in modules[m]['output']:
                if modules[o]['type'] == '&':
                    modules[o]['input'][m] = False
        self.modules = modules

    def get_state(self):
        state = []
        for m in self.modules:
            if self.modules[m]['type'] == '%':
                state.append(self.modules[m]['state'])
            elif self.modules[m]['type'] == '&':
                state += self.modules[m]['input'].values()
        return state

    def process(self):
        incoming = [(None, False, 'broadcaster')]
        pulses = [1, 0, 0, set()]
        while incoming:
            next = []
            for f,p,i in incoming:
                if i == 'rx' and p == False:
                    pulses[2] += 1

                m = self.modules[i]
                if m['type'] == 'B':
                    for o in m['output']:
                        next.append((i,p,o))
                        self.modules[o]['input'][i] = p
                    pulses[int(p)] += len(m['output'])
                elif m['type'] == '%':
                    if p == False:
                        m['state'] = not m['state']
                        for o in m['output']:
                            next.append((i,m['state'],o))
                            self.modules[o]['input'][i] = m['state']
                        pulses[int(m['state'])] += len(m['output'])
                elif m['type'] == '&':
                    m['input'][f] = p
                    p_new = not all(m['input'].values())
                    for o in m['output']:
                        next.append((i,p_new,o))
                        self.modules[o]['input'][i] = p_new
                    pulses[int(p_new)] += len(m['output'])
                    if p_new:
                        pulses[3].add(i)
                elif m['type'] == 'O':
                    pass
                else:
                    raise Exception('Unknown type')
            incoming = next.copy()
        return pulses

    def solve(self):
        c = [0, 0]
        for _ in range(1000):
            cc = self.process()
            c[0] += cc[0]
            c[1] += cc[1]
        return c[0]*c[1]

    def solve2(self):
        # &hb -> rx
        modules = [m for m in self.modules if 'hb' in self.modules[m]['output']]
        appearances = defaultdict(list)
        c = defaultdict(int)
        for i in range(1000000000000):
            cc = self.process()
            for m in modules:
                if m in cc[3]:
                    appearances[m].append(i)
                    if len(appearances[m]) > 1:
                        c[m] = appearances[m][-1] - appearances[m][-2]
            if len(c) == len(modules):
                break
        p = 1
        for i in c:
            p = p*c[i]//math.gcd(p,c[i])
        return p


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
