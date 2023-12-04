"""
Advent Of Code
--- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4
"""
from __future__ import annotations
import functools
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def count_win_numbers(self, n):
        return sum([1 if i in self.input[n][0] else 0 for i in self.input[n][1]])

    def count_points(self, n):
        x = self.count_win_numbers(n)
        return 0 if x == 0 else pow(2, x-1)

    def solve(self):
        return sum([self.count_points(c) for c in range(len(self.input))])

    def do_round(self, quantity):
        cards = [0]*len(self.input)
        for n in range(len(quantity)):
            x = self.count_win_numbers(n)
            for j in range(x):
                cards[n+j+1] += quantity[n]
        return cards

    def solve2(self):
        cards = [1] * len(self.input)
        s = 0
        while True:
            x = sum(cards)
            if x == 0:
                return s
            s += x
            cards = self.do_round(cards)


class Solver:
    def __init__(self, input) -> None:
        cards = []
        for line in input:
            _, win, have = parse.parse("Card {}: {} | {}", line)
            cards.append((list(map(int, win.split())), list(map(int, have.split()))))
        self.input = cards

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
