"""
Advent Of Code
--- Day 25: Snowverload ---
https://adventofcode.com/2023/day/25
"""
from __future__ import annotations
import random
import networkx as nx
from datetime import datetime


class Problem:
    def __init__(self, input) -> None:
        nodes = set()
        edges = []
        for line in input:
            link = line.replace(':', '').split()
            nodes.add(link[0])
            for node in link[1:]:
                nodes.add(node)
                edges.append((link[0], node))
        self.edges = edges
        self.nodes = nodes

    def contract(self):
        edges = self.edges.copy()
        nodes = dict((n,1) for n in self.nodes)
        while len(nodes) > 2:
            link = random.sample(list(edges), 1)[0]
            # print(link, nodes)
            nodes[link[0]] += nodes[link[1]]
            del nodes[link[1]]
            while link in edges:
                edges.remove(link)
            while (link[1], link[0]) in edges:
                edges.remove((link[1], link[0]))
            for n in nodes:
                if n == link[0]:
                    continue
                while (n, link[1]) in edges:
                    edges.remove((n, link[1]))
                    edges.append((n, link[0]))
                while (link[1], n) in edges:
                    edges.remove((link[1], n))
                    edges.append((link[0], n))
            # print(nodes)
            # print(len(edges), edges, '\n---')
        return nodes, edges


    def solve(self):
        c = 0
        while True:
            c += 1
            nodes, edges = self.contract()
            print(datetime.now().strftime("%H:%M:%S"), c, len(edges))
            if len(edges) == 3:
                break
        # print(nodes, edges)
        l = list(nodes.values())
        return l[0] * l[1]

    def solve2(self):
        n = nx.Graph()
        for edge in self.edges:
            n.add_edge(edge[0], edge[1])
        edges = nx.minimum_edge_cut(n)
        n.remove_edges_from(edges)
        a,b = nx.connected_components(n)
        return len(a)*len(b)


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
