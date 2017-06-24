"""
https://www.hackerrank.com/challenges/maximum-perimeter-triangle
"""

def is_valid(sides):
    _valid = (sides[0] + sides[1]) > sides[2]
    _valid = _valid and (sides[2] + sides[0] > sides[1])
    _valid = _valid and (sides[2] + sides[1] > sides[0])
    return _valid

def main():
    n = int(input().strip())
    l = sorted(map(int, input().strip().split()), reverse=True)
    maxperi = -1
    triangle = None
    for i in range(n-2):
        tri = (l[i], l[i+1], l[i+2])
        if is_valid(tri):
            if (triangle is None) or (sum(tri) > maxperi):
                triangle = tri
                maxperi = sum(tri)
            elif sum(tri) == maxperi:
                if max(tri) > max(triangle):
                    triangle = tri
                elif max(tri) == max(triangle) and min(tri) > min(triangle):
                    triangle = tri
    if triangle is not None:
        print(" ".join(map(str,sorted(triangle))))
    else:
        print(-1)

    
if __name__ == '__main__':
    main()