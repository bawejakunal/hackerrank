#!/bin/python
"""
https://www.hackerrank.com/challenges/the-grid-search
"""

def is_present(G, index, row, P):
    """
    First row of P found in G[row]
    confirm the complete pattern
    """
    try:
        for i in xrange(1, len(P)):
            end = index + len(P[i])
            if G[row + i][index:end] != P[i]:
                return False
        return True
    except ValueError:
        return False

def main():
    """
    grid pattern search
    """
    t = int(raw_input().strip())
    for _ in xrange(t):
        R, C = raw_input().strip().split(' ')
        R, C = [int(R), int(C)]
        G = list()
        G_i = 0
        for G_i in xrange(R):
            G_t = str(raw_input().strip())
            G.append(G_t)
        r, c = raw_input().strip().split(' ')
        r, c = [int(r), int(c)]
        P = list()
        P_i = 0
        for P_i in xrange(r):
            P_t = str(raw_input().strip())
            P.append(P_t)

        present = False
        for row in xrange(R - r + 1):
            """
            search for all indices within a row
            the pattern can be below any of the
            occurrences of P[0] in G[row]
            """
            index = 0
            while index < len(G[row]):
                index = G[row].find(P[0], index)
                if index == -1:
                    break
                if is_present(G, index, row, P):
                    present = True
                    break #out of while loop
                index += 1 #search from next index in same row

            if present is True:
                break #out of for loop, optimization

        print 'YES' if present else 'NO'


if __name__ == '__main__':
    main()
