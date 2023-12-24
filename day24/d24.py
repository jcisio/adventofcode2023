"""
Advent Of Code
--- Day 24: Never Tell Me The Odds ---
https://adventofcode.com/2023/day/24
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.stones = [parse.parse('{:d}, {:d}, {:d} @ {:d}, {:d}, {:d}',x).fixed for x in input]

    def intersect(self, a, b):
        if a[4]*b[3] == a[3]*b[4]:
            return None, None, None, None
        x = ((a[1]*a[3]-a[4]*a[0])/a[3] - (b[1]*b[3]-b[4]*b[0])/b[3]) / (b[4]/b[3] - a[4]/a[3])
        y = (a[1]*a[3]-a[4]*a[0])/a[3] + (a[4]/a[3])*x
        ta = (x-a[0])/a[3]
        tb = (x-b[0])/b[3]
        return x, y, ta, tb

    def count(self, min, max):
        s = 0
        for i in range(len(self.stones)):
            for j in range(i+1, len(self.stones)):
                x, y, ti, tj = self.intersect(self.stones[i], self.stones[j])
                if x == None:
                    continue
                if x >= min and x <= max and y >= min and y <= max and ti >= 0 and tj >= 0:
                    s += 1
        return s

    def solve(self):
        #return self.count(7, 27)
        return self.count(200000000000000, 400000000000000)

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
