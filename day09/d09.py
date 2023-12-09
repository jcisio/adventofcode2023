"""
Advent Of Code
--- Day 9: Mirage Maintenance ---
https://adventofcode.com/2023/day/9
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def extrapolate(self, seq):
        seqs = []
        seqs.append(seq)
        seq1 = seq.copy()
        while len(list(filter(lambda x: x != 0, seq1))) > 0:
            seq2 = [seq1[i+1]-seq1[i] for i in range(len(seq1)-1)]
            seqs.append(seq2.copy())
            seq1 = seq2

        seqs[-1].append(0)
        for i in range(len(seqs)-1, 0, -1):
            seqs[i-1].append(seqs[i][-1] + seqs[i-1][-1])
#        print(seqs[0][-1])
        return seqs[0][-1]

    def solve(self):
        return sum([self.extrapolate(line) for line in self.input])

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = [list(map(int, line.split())) for line in input]

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
