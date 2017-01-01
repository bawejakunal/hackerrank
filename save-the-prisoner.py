"""
https://www.hackerrank.com/challenges/save-the-prisoner
"""
def main():
    """
    Save the prisoner
    """
    T = int(raw_input().strip())
    while T > 0:
        N, M, S = map(int, raw_input().strip().split())
        M = M % N # adjust for wrap around of sweet distribution
        print ((S - 1 + M - 1) % N) + 1 #move M - 1 prisoners from first
        T -= 1

if __name__ == '__main__':
    main()

"""
The trick is to conver 1 index prisoner id to 0 indexed
and then apply modulo operations. Before final answer,
convert back to 1 indexed id numbers
"""