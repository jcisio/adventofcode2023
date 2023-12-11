"""
Advent Of Code
--- Day 10: Pipe Maze ---
https://adventofcode.com/2023/day/10
"""
from __future__ import annotations


class Problem:
    def __init__(self, input) -> None:
        self.grid = input['grid']
        self.start = input['start']
        self.rows = input['rows']
        self.cols = input['cols']
        self.raw = input['raw']
        self.loop = self.find_loop()

    def find_loop(self):
        grid = self.grid
        prev = None
        curr = self.start
        loop = [curr]
        while True:
            #print(curr)
            n1 = (curr[0] + grid[curr][0], curr[1] + grid[curr][1])
            n2 = (curr[0] + grid[curr][2], curr[1] + grid[curr][3])
            if n1 == prev:
                prev = curr
                curr = n2
            else:
                prev = curr
                curr = n1
            if curr == self.start:
                break
            loop.append(curr)
        return loop

    def solve(self):
        return len(self.loop)//2

    def count_r(self, p):
        s = 0
        for i in range(p[0]):
            rc = (i, p[1])
            if rc not in self.loop:
                continue
            if self.grid[rc] == (-1, 0, 1, 0):
                continue
            if self.grid[rc] == (0, -1, 0, 1):
                s += 1
            elif self.grid[rc] == (0, 1, -1, 0):
                s += 0.5
            elif self.grid[rc] == (1, 0, 0, -1):
                s += 0.5
            else:
                s -= 0.5
            #print(rc, self.grid[rc], s)
        return s

    def print_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (r,c) in self.loop:
                    print(self.raw[(r,c)], end='')
                else:
                    print('.', end='')
            print()

    def count_c(self, p):
        return sum([self.score_wall((p[0],j)) for j in range(p[1])])

    def is_inside(self, p):
        if p in self.loop:
            return 0
        #if self.count_r(p) % 2 == 1:
            #print(p, self.count_r(p))
        return 1 if self.count_r(p) % 2 == 1 else 0

    def solve2(self):
        #self.print_grid()
        #print(self.count_r((8,4)))
        return sum([self.is_inside((r,c)) for r in range(self.rows) for c in range(self.cols)])


class Solver:
    def __init__(self, input) -> None:
        grid = {}
        raw = {}
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
                    raw[(r, c)] = p
                elif p == 'S':
                    s = (r, c)
                    raw[s] = 'S'
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
                            #print(n)
        if len(connections) != 2:
            raise Exception("Invalid input")
        if (connections[0][0] - s[0], connections[0][1] - s[1], connections[1][0] - s[0], connections[1][1] - s[1]) in mapping.values():
            grid[s] = (connections[0][0] - s[0], connections[0][1] - s[1], connections[1][0] - s[0], connections[1][1] - s[1])
        else:
            grid[s] = (connections[1][0] - s[0], connections[1][1] - s[1], connections[0][0] - s[0], connections[0][1] - s[1])
        #print(grid[s])
        self.input = {'grid': grid, 'start': s, 'rows': len(input), 'cols': len(input[0]), 'raw': raw}

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
