"""
Advent Of Code
--- Day 18: Lavaduct Lagoon ---
https://adventofcode.com/2023/day/18
"""
from __future__ import annotations
from collections import deque
import parse


class Problem:
    def __init__(self, input) -> None:
        self.plan = input
        self.grid = {}

    def parse_step(self, step, part=1):
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if part == 1:
            return D['UDLR'.index(step[0])], step[1]
        return D['3120'.index(step[2][-1])], int(step[2][:-1], 16)

    def parse(self):
        here = (0, 0)
        for step in self.plan:
            d, length = self.parse_step(step)
            for i in range(length):
                self.grid[(here[0]+d[0]*(i+1), here[1]+d[1]*(i+1))] = True
            here = (here[0]+d[0]*step[1], here[1]+d[1]*step[1])
        self.r = min([x[0] for x in self.grid]), max([x[0] for x in self.grid])
        self.c = min([x[1] for x in self.grid]), max([x[1] for x in self.grid])

    def print(self):
        for r in range(self.r[0], self.r[1]+1):
            for c in range(self.c[0], self.c[1]+1):
                print('#' if (r,c) in self.grid else ' ', end='')
            print()

    def count(self):
        #self.print()
        for r in range(self.r[0], self.r[1]+1):
            if (r,self.c[0]) not in self.grid:
                self.fill(r,self.c[0])
            if (r,self.c[1]) not in self.grid:
                self.fill(r,self.c[1])
        for c in range(self.c[0], self.c[1]+1):
            if (self.r[0],c) not in self.grid:
                self.fill(self.r[0],c)
            if (self.r[1],c) not in self.grid:
                self.fill(self.r[1],c)
        return (self.r[1] - self.r[0] +1) * (self.c[1] - self.c[0]+1) - sum([1 for x in self.grid if self.grid[x]==False])

    def fill(self, r, c):
        q = deque([(r,c)])
        while q:
            r,c = q.popleft()
            if (r,c) in self.grid:
                continue
            if self.r[0] > r or r > self.r[1] or self.c[0] > c or c > self.c[1]:
                continue
            self.grid[(r,c)] = False
            for d in [(0,-1), (0,1), (-1,0), (1,0)]:
                q.append((r+d[0], c+d[1]))

    def solve(self):
        self.parse()
        return self.count()

    def solve2(self):
        here = (0, 0)
        P = []
        border = 0
        for step in self.plan:
            d, length = self.parse_step(step, 2)
            here = (here[0]+d[0]*length, here[1]+d[1]*length)
            P.append(here)
            border += length
        P.append(P[0])
        s = abs(sum(r1*c2 - r2*c1 for (r1,c1),(r2,c2) in zip(P, P[1:])))//2 + border//2 + 1
        return s


class Solver:
    def __init__(self, input) -> None:
        self.input = [parse.parse('{:w} {:d} (#{})', line).fixed for line in input]

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
#print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
