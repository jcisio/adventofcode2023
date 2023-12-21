"""
Advent Of Code
--- Day 21: Step Counter ---
https://adventofcode.com/2023/day/21
"""
from __future__ import annotations
from collections import defaultdict


class Problem:
    def __init__(self, input) -> None:
        blocks = set()
        for r,line in enumerate(input):
            for c,p in enumerate(line):
                if p == '#':
                    blocks.add((r,c))
                elif p == 'S':
                    start = (r,c)
        self.blocks = blocks
        self.start = start
        self.r = len(input)
        self.c = len(input[0])

    def move(self, current):
        new = set()
        for r,c in current:
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = r+dr,c+dc
                if 0 <= nr < self.r and 0 <= nc < self.c and (nr,nc) not in self.blocks:
                    new.add((nr,nc))
        return new

    # Number of tiles reached after s steps
    def count(self, start, steps):
        c = set([start])
        for _ in range(steps):
            c = self.move(c)
        return len(c)


    def solve(self):
        return self.count(self.start, 64)

    def solve2(self, M=26501365):
        assert self.r == self.c
        R = self.r

        l = M//R # l is even: 202300
        r = R//2

        # complete tiles
        c_odd = (l-1)**2
        c_even = l**2

        # incomplete tiles
        i_bl = self.count((R-1,0), r-1)
        i_tl = self.count((0,0), r-1)
        i_tr = self.count((0,R-1), r-1)
        i_br = self.count((R-1,R-1), r-1)
        ix_bl = self.count((R-1,0), 3*r)
        ix_tl = self.count((0,0), 3*r)
        ix_tr = self.count((0,R-1), 3*r)
        ix_br = self.count((R-1,R-1), 3*r)

        # 4 corners
        corners = self.count((0, r), R-1) \
            + self.count((r, 0), R-1) \
            + self.count((R-1, r), R-1) \
            + self.count((r, R-1), R-1)

        return c_odd * self.count((r,r), R*2-1) \
            + c_even * self.count((r,r), R*2) \
            + l * (i_bl + i_tl + i_tr + i_br) \
            + (l-1) * (ix_bl + ix_tl + ix_tr + ix_br) \
            + corners
# 593177780427593 is too high
# 593168996149761 is too low
# 593174156999363 not right
# 593174079316436 not right
# 593174122420825

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
