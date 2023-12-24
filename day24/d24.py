"""
Advent Of Code
--- Day 24: Never Tell Me The Odds ---
https://adventofcode.com/2023/day/24
"""
from __future__ import annotations
import parse
import math
from collections import Counter


class Problem:
    def __init__(self, input) -> None:
        self.stones = [parse.parse('{:d}, {:d}, {:d} @ {:d}, {:d}, {:d}',x).fixed for x in input]

    def intersect(self, a, b):
        if a[4]*b[3] == a[3]*b[4]:
            return None, None, None, None
        x = ((a[1]*a[3]-a[4]*a[0])/a[3] - (b[1]*b[3]-b[4]*b[0])/b[3]) / (b[4]/b[3] - a[4]/a[3])
        y = (a[1]*a[3]-a[4]*a[0])/a[3] + (a[4]/a[3])*x
        ta = (x-a[0])/a[3]
        tb = (x-b[0])/b[3]
        return x, y, ta, tb

    def count(self, min, max):
        s = 0
        for i in range(len(self.stones)):
            for j in range(i+1, len(self.stones)):
                x, y, ti, tj = self.intersect(self.stones[i], self.stones[j])
                if x == None:
                    continue
                if x >= min and x <= max and y >= min and y <= max and ti >= 0 and tj >= 0:
                    s += 1
        return s

    def solve(self):
        #return self.count(7, 27)
        return self.count(200000000000000, 400000000000000)

    def gcd(self, v, dim):
        stones = [s for s in self.stones if s[3+dim] == v]
        delta = []
        for i in range(len(stones)-1):
            for j in range(i+1, len(stones)):
                delta.append(stones[j][dim]-stones[i][dim])
        gcd = delta[0]
        for i in range(1, len(delta)):
            gcd = math.gcd(gcd, delta[i])
        return gcd

    def solve_dim(self, dim):
        count = Counter()
        for s in self.stones:
            count[s[3+dim]] += 1
        for c,_ in count.most_common(1):
            stones = [s for s in self.stones if s[3+dim] == c]
            delta = []
            for i in range(len(stones)-1):
                for j in range(i+1, len(stones)):
                    delta.append(stones[j][dim]-stones[i][dim])
            gcd = delta[0]
            for i in range(1, len(delta)):
                gcd = math.gcd(gcd, delta[i])
            v = stones[0][3+dim] - gcd

        stones = sorted(self.stones, key=lambda x: x[3+dim])
        for s in stones: print(s)

        # Same direction
        s_right = [s[dim] for s in stones if s[3+dim] < v and s[3+dim] * v > 0]
        s_left = [s[dim] for s in stones if s[3+dim] > v and s[3+dim] * v > 0]
        s_min = max(s_left) if s_left else -1e20
        s_max = min(s_right) if s_right else 1e20

        # Inverse direction
        if v < 0:
            id_min = max([s[dim] for s in stones if s[3+dim] > 0])
            s_min = min(s_min, id_min)
        else:
            id_min = min([s[dim] for s in stones if s[3+dim] < 0])
            s_max = max(s_max, id_min)

        print(s_min, s_max)


    def solve2(self):
        self.solve_dim(0)
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
#print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
