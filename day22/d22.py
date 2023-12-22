"""
Advent Of Code
--- Day 22: Sand Slabs ---
https://adventofcode.com/2023/day/22
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.bricks = list(map(lambda x: parse.parse("{:d},{:d},{:d}~{:d},{:d},{:d}", x).fixed, input))
        for b in self.bricks:
            # Brick must be aligned with one of the axes
            assert (b[0]==b[3] and b[1] == b[4]) or (b[0]==b[3] and b[2] == b[5]) or (b[1]==b[4] and b[2] == b[5])
            # Coordinate is sorted
            assert b[0] <= b[3] and b[1] <= b[4] and b[2] <= b[5]
        self.bricks.sort(key=lambda b: b[2])
        # Name it to debug order
        for i in range(len(self.bricks)):
            self.bricks[i] += (chr(i+65),)

    def add_spaces(self, spaces, brick):
        for x in range(brick[0], brick[3]+1):
            for y in range(brick[1], brick[4]+1):
                for z in range(brick[2], brick[5]+1):
                    spaces.add((x,y,z))
        #print(spaces)

    def can_fall(self, spaces, brick):
        d = 0
        for dz in range(1, brick[2]):
            for x in range(brick[0], brick[3]+1):
                stop = False
                for y in range(brick[1], brick[4]+1):
                    if (x, y, brick[2]-dz) in spaces:
                        stop = True
                        break
                if stop: break
            if stop: break
            d = dz
        return d

    def is_holding(self, b1, b2):
        for x in range(b1[0], b1[3]+1):
            for y in range(b1[1], b1[4]+1):
                if b2[0] <= x <= b2[3] and b2[1] <= y <= b2[4] and b2[2] == b1[5] + 1:
                    return True
        return False

    def falling_down(self):
        s = 0
        spaces = set()
        # Falling down
        for i, b in enumerate(self.bricks):
            dz = self.can_fall(spaces, b)
            if dz > 0:
                b = (b[0], b[1], b[2]-dz, b[3], b[4], b[5]-dz, b[6])
                #print(f'Brick {b[6]} fell down {dz}')
                s += 1
            self.bricks[i] = b
            self.add_spaces(spaces, b)
        return s

    def solve(self):
        self.falling_down()
        self.bricks.sort(key=lambda b: b[2])

        holders = defaultdict(list)
        for i, b in enumerate(self.bricks):
            for j in range(i+1, len(self.bricks)):
                if self.is_holding(b, self.bricks[j]):
                    #print(f'{b[6]} is holding {self.bricks[j][6]}')
                    holders[j].append(i)

        s = 0
        #print(holders)
        for i in range(len(self.bricks)):
            ok = True
            for h in holders:
                if i in holders[h] and len(holders[h]) == 1:
                    ok = False
                    break
            s += int(ok)
        return s

    def solve2(self):
        self.falling_down()
        bricks = self.bricks.copy()
        s = 0
        for i in range(len(bricks)):
            self.bricks = bricks[:i] + bricks[i+1:]
            #print(self.bricks)
            s += self.falling_down()
        return s


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
