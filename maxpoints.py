"""
"""

def __maxPoints__(soln, elements):
    if len(elements) < 1:
        return 0
    
    if elements[-1] in soln:
        return soln[elements[-1]]

    num = elements.pop()
    points = num
    alt = 0

    while len(elements) > 0 and elements[-1] == num:
        elements.pop()
        points += num

    if len(elements) > 0 and elements[-1] == num - 1:
        alt = __maxPoints__(soln, elements.copy())

    while len(elements) > 0 and elements[-1] == num - 1:
        elements.pop()
    points += __maxPoints__(soln, elements)

    soln[num] = max(points, alt)
    return soln[num]

def maxPoints(elements):
    elements.sort()
    soln = dict()
    return __maxPoints__(soln, elements)


def main():
    elements = list(map(int, input().split()))
    print(maxPoints(elements))

if __name__ == '__main__':
    main()
