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

    def get_type(self, hand, part=1):
        types = defaultdict(int)
        for card in hand:
            types[card] += 1
        if len(types) == 1:
            return 7
        if len(types) == 2:
            if part == 2 and 'J' in types:
                return 7
            if max(types.values()) == 4:
                return 6
            return 5
        if len(types) == 3:
            if part == 2:
                if types['J'] == 3:
                    return 6
                if types['J'] == 2:
                    return 6
                if types['J'] == 1:
                    return 6 if max(types.values()) == 3 else 5
            if max(types.values()) == 3:
                return 4
            return 3
        if len(types) == 4:
            if part == 2:
                if 'J' in types:
                    return 4
            return 2
        if part == 2 and 'J' in types:
            return 2
        return 1


    def get_score(self, hand, part=1):
        score = self.get_type(hand) if part == 1 else self.get_type(hand, part)
        for card in hand:
            score = score * 20 + ('23456789TJQKA' if part ==1 else 'J23456789TQKA').index(card)
        return score

    def solve(self, part):
        hands = sorted(self.input, key=lambda x: self.get_score(x[0], part))
        s = 0
        for i, hand in enumerate(hands):
            s += hand[1]*(i+1)
            #print(f'{hand[0]} {self.get_type(hand[0], part)}')
        return s


class Solver:
    def __init__(self, input) -> None:
        self.input = [parse.parse('{} {:d}',line).fixed for line in input]

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve(part)


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
