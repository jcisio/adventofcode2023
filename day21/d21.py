"""
Advent Of Code
--- Day 21: Step Counter ---
https://adventofcode.com/2023/day/21
"""
from __future__ import annotations
from collections import defaultdict
import parse


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

    def solve(self):
        s = set([self.start])
        for _ in range(64):
            s = self.move(s)
        return len(s)

    def solve2(self, M=5001):
        assert self.r == self.c
        R = self.r
        # Suppose that we can reach any point from any point after these steps:
        l = self.r + self.c
        corners = [(0,0),(0,self.c-1),(self.r-1,0),(self.r-1,self.c-1)]
        # From a corner how many we can reach for a number of steps?
        d_corners = defaultdict(list)
        for c in corners:
            s = set([c])
            for _ in range(l-1):
                s = self.move(s)
                d_corners[c].append(len(s))
        # We also know that l is even, each edge length is odd
        spots = (d_corners[c][-2], d_corners[c][-1])
        print(spots)
        # How many steps we need to reach a corner from S?
        s_corners = {}
        s = set([self.start])
        for i in range(l):
            s = self.move(s)
            for c in corners:
                if c in s and c not in s_corners:
                    s_corners[c] = i+1
        # In my input, edge length is 131, each corner needs exactly 130 steps
        #print(s_corners)
        # Number of tiles we control completely
        N = (M - max(s_corners.values()))//R
        tiles = N*(N-1)*2 + N*4 + 1
        partials = (N+1)*4
        print(self.r, self.c, len(self.blocks))
        return tiles*spots[M%2] + partials*d_corners[(0,0)][(M - max(s_corners.values())) % R]


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
#print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
