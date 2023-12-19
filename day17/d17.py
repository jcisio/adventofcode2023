"""
Advent Of Code
--- Day 17: Clumsy Crucible ---
https://adventofcode.com/2023/day/17
"""
from __future__ import annotations
from colorama import Fore, Back, Style
from collections import defaultdict
import heapq

class Problem:
    MAX = 9999
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DIR = [UP, DOWN, LEFT, RIGHT]

    def __init__(self, input) -> None:
        self.r = len(input)
        self.c = len(input[0])
        self.blocks = {}
        self.distance = defaultdict(lambda: defaultdict(lambda: self.MAX))
        for r, line in enumerate(input):
            for c, char in enumerate(line):
                self.blocks[(r, c)] = int(char)
        self.distance[(0,0)] = 0


    def t(self, d):
        return '<' if d == self.LEFT else '>' if d == self.RIGHT else '^' if d == self.UP else 'v'

    def solve(self, smin=1, smax=3):
        next = []
        visited = set()
        heapq.heappush(next, (0, (0,0), self.RIGHT))
        heapq.heappush(next, (0, (0,0), self.DOWN))
        distance = defaultdict(lambda: self.MAX)
        distance[((0,0), self.RIGHT)] = 0
        distance[((0,0), self.DOWN)] = 0
        while next:
            dist, (r, c), d = heapq.heappop(next)
            if ((r,c), d) in visited:
                continue

            if (r, c) == (self.r-1, self.c-1):
                return distance[((r,c), d)]
            visited.add(((r,c), d))

            for nd in self.DIR:
                if nd == d or nd == (-d[0], -d[1]):
                    continue
                for i in range(smin,smax+1):
                    nr, nc = r + nd[0]*i, c + nd[1]*i
                    if not (0 <= nr < self.r and 0 <= nc < self.c):
                        continue
                    s = sum([self.blocks[((r+nd[0]*j, c+nd[1]*j))] for j in range(1,i+1)])
                    distance[((nr, nc), nd)] = min(distance[((nr, nc), nd)], distance[((r,c), d)] + s)
                    #print(r, c, d, nr, nc, nd, s, f'Distance to {(nr,nc)} {self.t(nd)}: {distance[((nr, nc), nd)]}')
                    heapq.heappush(next, (dist + s, (nr, nc), nd))

    def solve2(self):
        return self.solve(4, 10)


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
