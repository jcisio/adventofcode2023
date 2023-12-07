"""
Advent Of Code
--- Day 7: Camel Cards ---
https://adventofcode.com/2023/day/7
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def get_type(self, hand):
        types = defaultdict(int)
        for card in hand:
            types[card] += 1
        if len(types) == 1:
            return 7
        if len(types) == 2:
            if max(types.values()) == 4:
                return 6
            return 5
        if len(types) == 3:
            if max(types.values()) == 3:
                return 4
            return 3
        if len(types) == 4:
            return 2
        return 1

    def get_score(self, hand):
        score = self.get_type(hand)
        for card in hand:
            score = score * 20 + '23456789TJQKA'.index(card)
        return score

    def solve(self):
        hands = sorted(self.input, key=lambda x: self.get_score(x[0]))
        print(hands)
        s = 0
        for i, hand in enumerate(hands):
            s += hand[1]*(i+1)
        return s

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = [parse.parse('{} {:d}',line).fixed for line in input]

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
