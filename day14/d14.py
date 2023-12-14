"""
Advent Of Code
--- Day 14: Parabolic Reflector Dish ---
https://adventofcode.com/2023/day/14
"""
class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def tilt(self, direction):
        rounded = self.input['rounded']
        if direction == 'north':
            for c in range(self.input['c']):
                free = 0
                for r in range(self.input['r']):
                    cell = (r, c)
                    if cell in self.input['cubed']:
                        free = r + 1
                    elif cell in rounded:
                        if free < r:
                            rounded.remove(cell)
                            rounded.append((free, c))
                        free += 1
        elif direction == 'south':
            for c in range(self.input['c']):
                free = self.input['r'] - 1
                for r in range(self.input['r'], -1, -1):
                    cell = (r, c)
                    if cell in self.input['cubed']:
                        free = r - 1
                    elif cell in rounded:
                        if free > r:
                            rounded.remove(cell)
                            rounded.append((free, c))
                        free -= 1
        elif direction == 'east':
            for r in range(self.input['r']):
                free = self.input['c'] - 1
                for c in range(self.input['c'], -1, -1):
                    cell = (r, c)
                    if cell in self.input['cubed']:
                        free = c - 1
                    elif cell in rounded:
                        if free > c:
                            rounded.remove(cell)
                            rounded.append((r, free))
                        free -= 1
        elif direction == 'west':
            for r in range(self.input['r']):
                free = 0
                for c in range(self.input['c']):
                    cell = (r, c)
                    if cell in self.input['cubed']:
                        free = c + 1
                    elif cell in rounded:
                        if free < c:
                            rounded.remove(cell)
                            rounded.append((r, free))
                        free += 1
    def do_cycle(self):
        self.tilt('north')
        self.tilt('west')
        self.tilt('south')
        self.tilt('east')

    def state(self):
        s = ''
        for r in range(self.input['r']):
            for c in range(self.input['c']):
                cell = (r, c)
                if cell in self.input['cubed']:
                    s += '#'
                elif cell in self.input['rounded']:
                    s += 'O'
                else:
                    s += '.'
            s += '\n'
        return s

    def score(self, state = None):
        if not state:
            state = self.state()
        score = 0
        for i, c in enumerate(state):
            if c == 'O':
                score += self.input['r'] - i // (self.input['c'] + 1)
        return score


    def solve(self):
        self.tilt('north')
        return self.score()

    def solve2(self):
        states = []
        N = 1000000000
        i = 0
        while i < N:
            self.do_cycle()
            state = self.state()
            try:
                idx = states.index(state)
                return self.score(states[(N-i-1) % (i - idx) + idx])
            except ValueError:
                states.append(state)
            i += 1


class Solver:
    def __init__(self, input) -> None:
        rounded = []
        cubed = []
        for r, line in enumerate(input):
            for c, rock in enumerate(line):
                if rock == '#':
                    cubed.append((r, c))
                elif rock == 'O':
                    rounded.append((r, c))
        self.input = {'rounded': rounded, 'cubed': cubed, 'r': len(input), 'c': len(input[0])}

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
