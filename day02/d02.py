"""
Advent Of Code
--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2
"""
from __future__ import annotations
import functools
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self):
        s = 0
        for i in range(0, len(self.input)):
            game = self.input[i]
            if all(map(lambda x: x['red'] <= 12 and x['green'] <= 13 and x['blue'] <= 14, game)):
                s += i + 1
        return s

    def solve2(self):
        s = 0
        for i in range(0, len(self.input)):
            game = self.input[i]
            m = [max([cubes[c] for cubes in game]) for c in ('red', 'green', 'blue')]
            s += m[0]*m[1]*m[2]
        return s


class Solver:
    def __init__(self, input) -> None:
        games = []
        for line in input:
            picks = parse.parse('Game {:d}: {}', line)[1].split(';')
            game = []
            for pick in picks:
                cubes = dict(map(lambda x: reversed(parse.parse('{:d} {:w}', x).fixed), pick.split(', ')))
                game.append({'red': 0, 'green': 0, 'blue': 0} | cubes)
            games.append(game)
        self.input = games

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
