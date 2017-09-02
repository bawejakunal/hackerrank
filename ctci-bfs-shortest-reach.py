"""
https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
"""

from collections import deque

class Graph(object):
    def __init__(self, nodes):
        self.weight = 6
        self.nodes = nodes
        self.edges = [set() for i in range(self.nodes)]
    
    def connect(self, x, y):
        self.edges[x].add(y)
        self.edges[y].add(x)
    
    def find_all_distances(self, s):
        dist = [-1 for i in range(self.nodes)]
        q = deque()
        q.append(s)
        dist[s] = 0     # distance from self
        
        while len(q) > 0:
            node = q.popleft()
            for nbr in self.edges[node]:
                if dist[nbr] == -1:
                    dist[nbr] = self.weight + dist[node]
                    q.append(nbr)
        del dist[s]
        return dist

def main():
    t = int(input())
    for i in range(t):
        n,m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            graph.connect(x-1,y-1) 
        s = int(input())
        print(" ".join(map(str, graph.find_all_distances(s-1))))

if __name__ == '__main__':
    main()
    
