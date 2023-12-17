"""
Advent Of Code
--- Day 17: Clumsy Crucible ---
https://adventofcode.com/2023/day/17
"""
from __future__ import annotations
from colorama import Fore, Back, Style
from collections import defaultdict

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
        self.distance = {}
        self.updates = defaultdict(list)
        for r, line in enumerate(input):
            for c, char in enumerate(line):
                self.blocks[(r, c)] = int(char)
                # direction, continous blocks
                self.distance[(r,c)] = {self.UP: (self.MAX, 0), self.DOWN: (self.MAX, 0), self.LEFT: (self.MAX, 0), self.RIGHT: (self.MAX, 0)}
        for d in self.DIR:
            self.distance[(0,0)][d] = (0, 0)

    def min(self, r, c):
        return min([self.distance[(r,c)][d][0] for d in self.DIR])

    def t(self, d):
        return '<' if d == self.LEFT else '>' if d == self.RIGHT else '^' if d == self.UP else 'v'

    def print(self, r, c):
        return f'{Fore.GREEN}{r}, {c}{Fore.RESET} [' + ', '.join([f'{self.t(d)} {self.distance[(r,c)][d][0]} ({self.distance[(r,c)][d][1]})' for d in self.DIR if 0 < self.distance[(r,c)][d][0] < self.MAX]) + ']'

    def print_trace(self, r, c):
        d = min(self.DIR, key=lambda d: self.distance[(r,c)][d][0])
        trace = {}
        remain_distance = self.distance[(r,c)][d][0]
        print(f'Total distance {remain_distance} to {self.print(r,c)}')
        while not (r == 0 and c == 0):
            remain_distance -= self.blocks[(r,c)]
            print(remain_distance)
            r -= d[0]
            c -= d[1]
            d = [d for d in self.DIR if self.distance[(r,c)][d][0] == remain_distance][0]
            trace[(r,c)] = d

        for r,c in reversed(trace):
            print(self.t(trace[(r,c)]), self.print(r,c))

        for r in range(self.r):
            for c in range(self.c):
                print(Fore.GREEN+self.t(trace[(r,c)])+Fore.RESET if (r, c) in trace else self.blocks[(r,c)], end='')
            print()

    def print_updates(self, r, c):
        print(f'Updates for ({r},{c})')
        for u in self.updates[(r,c)]:
            print('\t', u)

    def solve(self):
        next = [(0,0)]
        visited = []
        while True:
            r, c = next.pop(0)
            visited.append((r,c))
            for d in self.DIR:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nr >= self.r or nc < 0 or nc >= self.c:
                    continue
                for cd in self.DIR:
                #for cd in [d]:
                    # Can't go back
                    if d[0]+cd[0] == 0 and d[1]+cd[1] == 0:
                        continue
                    if self.distance[(nr, nc)][d][0] > self.blocks[(nr, nc)] + self.distance[(r,c)][cd][0]:
                        if d != cd or self.distance[(r, c)][cd][1] < 3:
                            print(f'From {self.print(r,c)} ({self.t(cd)}) to {self.print(nr,nc)} using {Style.BRIGHT}{self.t(d)}{Style.NORMAL}')
                            print(f'     distance on {self.t(d)} from {self.distance[(nr, nc)][d]}', end='')
                            self.distance[(nr, nc)][d] = (self.blocks[(nr, nc)] + self.distance[(r,c)][cd][0], self.distance[(r,c)][cd][1] + 1 if d == cd else 1)
                            self.updates[(nr, nc)].append(f'From ({r},{c}) {self.t(d)} from block distance {self.distance[(r,c)][cd]} to block distance {self.distance[(nr, nc)][d]}')
                            print(f' to {self.distance[(nr, nc)][d]}')
                            if (nr, nc) not in next:
                                next.append((nr, nc))
            if not next:
                break
            for r in range(self.r):
                for c in range(self.c):
                    if (r, c) in visited + next:
                        pass
                        #print(self.print(r,c))

        self.print_trace(0,6)
        self.print_updates(0,6)
#        self.print_trace(2,10)
        #self.print_trace(self.r-1, self.c-1)
        return self.min(self.r-1, self.c-1)

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
