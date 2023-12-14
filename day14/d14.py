"""
Advent Of Code
--- Day 14: Parabolic Reflector Dish ---
https://adventofcode.com/2023/day/14
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self):
        rounded = self.input['rounded'].copy()
        for c in range(self.input['c']):
            top = 0
            for r in range(self.input['r']):
                cell = (r, c)
                if cell in self.input['cubed']:
                    top = r + 1
                elif cell in rounded:
                    if top < r:
                        rounded.remove(cell)
                        rounded.append((top, c))
#                        print(f"({r}, {c}) -> ({top}, {c})")
                    top += 1
        score = 0
        for r, c in rounded:
            score += self.input['r'] - r
        return score

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        rounded = []
        cubed = []
        for r, line in enumerate(input):
            for c, rock in enumerate(line):
                if rock == '#':
                    cubed.append((r, c))
                elif rock == 'O':
                    rounded.append((r, c))
        self.input = {'rounded': rounded, 'cubed': cubed, 'r': len(input), 'c': len(input[0])}

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
