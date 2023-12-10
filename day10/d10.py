"""
Advent Of Code
--- Day 10: Pipe Maze ---
https://adventofcode.com/2023/day/10
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self):
        grid = self.input['grid']
        c = 0
        prev = None
        curr = self.input['start']
        while True:
            print(curr)
            n1 = (curr[0] + grid[curr][0], curr[1] + grid[curr][1])
            n2 = (curr[0] + grid[curr][2], curr[1] + grid[curr][3])
            if n1 == prev:
                prev = curr
                curr = n2
            else:
                prev = curr
                curr = n1
            if curr == self.input['start']:
                break
            c += 1
        return (c + 1)//2

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        grid = {}
        s = None
        mapping = {
            '|': (-1, 0, 1, 0),
            '-': (0, -1, 0, 1),
            'L': (0, 1, -1, 0),
            'J': (0, -1, -1, 0),
            '7': (1, 0, 0, -1),
            'F': (1, 0, 0, 1),
        }
        for r in range(len(input)):
            for c in range(len(input[r])):
                p = input[r][c]
                if p in mapping:
                    grid[(r, c)] = mapping[p]
                elif p == 'S':
                    s = (r, c)
        # Determine value of S
        connections = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i, j) != (0, 0):
                    n = (s[0] + i, s[1] + j)
                    if n in grid:
                        #print(n, grid[n], (grid[n][0] + n[0], grid[n][1] + n[1]), (grid[n][2] + n[0], grid[n][3] + n[1]), s)
                        if (grid[n][0] + n[0], grid[n][1] + n[1]) == s or (grid[n][2] + n[0], grid[n][3] + n[1]) == s:
                            connections.append(n)
        if len(connections) != 2:
            raise Exception("Invalid input")
        grid[s] = (connections[0][0] - s[0], connections[0][1] - s[1], connections[1][0] - s[0], connections[1][1] - s[1])
        self.input = {'grid': grid, 'start': s}

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
