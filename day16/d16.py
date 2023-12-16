"""
Advent Of Code
--- Day 16: The Floor Will Be Lava ---
https://adventofcode.com/2023/day/16
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    EMPTY = 0
    NOT_VISITED = 1
    VISITED = 2

    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

    def __init__(self, input) -> None:
        self.R = input['R']
        self.C = input['C']
        self.grid = {}
        for r in range(self.R):
            for c in range(self.C):
                # tile, right, down, left, up
                self.grid[(r, c)] = [input['grid'][r][c], self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY]
        # Beam arrive at (0,0) to the right
        self.grid[(0, 0)][1] = self.NOT_VISITED

    def energized(self, tile):
        return sum(tile[1:]) > 0

    def print(self):
        for r in range(self.R):
            for c in range(self.C):
                print('#' if self.energized(self.grid[(r,c)]) else '.', end='')
            print()

    def solve(self):
        while True:
            updated = False
            for rc, tile in self.grid.items():
                for i in range(1, 5):
                    if tile[i] == self.NOT_VISITED:
                        tile[i] = self.VISITED
                        updated = True
                        if (tile[0] == '|' and i in [self.RIGHT,self.LEFT]) or (tile[0] == '-' and i in [self.UP,self.DOWN]):
                            next = [self.RIGHT, self.LEFT] if i in [self.UP,self.DOWN] else [self.UP, self.DOWN]
                        elif tile[0] == '/':
                            next = [[self.UP,self.LEFT,self.DOWN,self.RIGHT][i-1]]
                        elif tile[0] == '\\':
                            next = [[self.DOWN,self.RIGHT, self.UP, self.LEFT][i-1]]
                        else:
                            next = [i]
                        #print(f'{rc} {tile} {i} {next}')
                        for n in next:
                            dr, dc = [(0,1), (1,0), (0,-1), (-1,0)][n-1]
                            if (rc[0]+dr, rc[1]+dc) in self.grid:
                                if self.grid[(rc[0]+dr, rc[1]+dc)][n] != self.VISITED:
                        #            print(' -> next ', (rc[0]+dr, rc[1]+dc))
                                    self.grid[(rc[0]+dr, rc[1]+dc)][n] = self.NOT_VISITED
            if not updated:
                break
        #self.print()
        return sum([1 for tile in self.grid.values() if self.energized(tile) > 0])

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = {'grid': input, 'R': len(input), 'C': len(input[0])}

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
