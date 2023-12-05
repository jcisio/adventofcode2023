"""
Advent Of Code
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5
"""
from __future__ import annotations
from collections import defaultdict


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def next_destination(self, v, mapping):
        for m in mapping:
            if m[1] <= v < m[1] + m[2]:
                return m[0] + v - m[1]
        return v

    def last_destination(self, v):
        for m in self.input['maps']:
            v = self.next_destination(v, self.input['maps'][m])
        return v

    def split_range(self, r, mapping):
        result = []
        for m in mapping:
            # 57,13 => (49, 53, 8), (61, 61, 9999999999)
            if r[0] < m[1] and m[1] < r[0] + r[1]:
                result.append((m[0], min(m[2], r[0] + r[1] - m[1])))
            elif m[1] <= r[0] < m[1] + m[2]:
                result.append((m[0] + r[0] - m[1], min(r[0] + r[1], m[1] + m[2]) - r[0]))
        #print(r, result)
        return result

    def next_range(self, ranges, mapping):
        result = []
        #print("Input ", ranges, "Mapping", mapping)
        for r in ranges:
            result += self.split_range(r, mapping)
        return sorted(result, key=lambda x: x[1])

    def last_range(self, seed):
        ranges = [(seed[i*2], seed[i*2+1]) for i in range(len(seed)//2)]
        for m in self.input['maps']:
            ranges = self.next_range(ranges, self.input['maps'][m])
        return ranges

    def solve(self):
        return min([self.last_destination(seed) for seed in self.input['seeds']])

    def solve2(self):
        return sorted(self.last_range(self.input['seeds']), key=lambda x: x[0])[0][0]


class Solver:
    def __init__(self, input) -> None:
        data = {'seeds': list(map(int, input[0].split(': ')[1].split())), 'maps': defaultdict(list)}
        current_map = None
        for line in input[2:]:
            if not line: continue
            if line.endswith(' map:'):
                current_map = line[:-5]
            else:
                data['maps'][current_map].append(tuple(map(int, line.split())))
        for _,v in data['maps'].items():
            v.sort(key=lambda x: x[1])
            l = len(v)
            # Add implicit ranges
            for i in range(l):
                start = 1 if i == 0 else v[i-1][1] + v[i-1][2]
                end = v[i][1] - 1
                if start <= end:
                    v.append((start, start, end - start + 1))
            v.sort(key=lambda x: x[1])
            v.append((v[-1][1] + v[-1][2], v[-1][1] + v[-1][2], 9999999999))
        self.input = data

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
