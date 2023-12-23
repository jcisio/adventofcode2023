"""
Advent Of Code
--- Day 23: A Long Walk ---
https://adventofcode.com/2023/day/23
"""
from __future__ import annotations


class Problem:
    def __init__(self, input) -> None:
        self.input = input
        self.r, self.c = len(input), len(input[0])

    def solve(self):
        Q = [((1,1), set([(0,1)]), 1)]
        end = (self.r-1, self.c-2)
        next = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
        M = 0
        while Q:
            pos, visited, steps = Q.pop()
            if pos in visited:
                continue
            if pos == end:
                if steps > M:
                    M = steps
                continue
            visited.add(pos)
            # c = self.input[pos[0]][pos[1]]
            # if c in next:
            #     Q.append(((pos[0]+next[c][0], pos[1]+next[c][1]), visited.copy(), steps+1))
            #     continue
            while True:
                candidate = []
                for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    new = (pos[0]+d[0], pos[1]+d[1])
                    if new in visited or self.input[new[0]][new[1]] == '#':
                        continue
                    candidate.append(new)
                if len(candidate) == 0:
                    break
                if len(candidate) > 1:
                    for new in candidate:
                        Q.append((new, visited.copy(), steps+1))
                    break
                else:
                    pos = candidate[0]
                    visited.add(pos)
                    steps += 1
                    if pos == end:
                        if steps > M:
                            M = steps
                        break
        return M

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
