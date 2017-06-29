import sys
sys.setrecursionlimit(10000)

def get_sequence(memo, attempt):
    for i in range(len(attempt)+1, 0, -1):
        if attempt[:i] in memo:
            # hold current in _seq
            _seq = [attempt[:i]]
            if attempt[i:] != "":
                _subseq = get_sequence(memo, attempt[i:]) # recursive
                if _subseq is not None:
                    _seq.extend(_subseq)
                    return _seq # this is the solution
            else:
                return _seq
    return None

def main():
    T = int(input().strip())
    while T > 0:
        N = int(input().strip())
        passwords = input().strip().split() # conver to hash set
        login_attempt = input().strip()
        memo = dict()
        for password in passwords:
            memo[password] = [password]
        sequence = get_sequence(memo, login_attempt)
        if sequence is not None:
            print(" ".join(sequence))
        else:
            print('WRONG PASSWORD')
        T  -= 1

if __name__ == '__main__':
    main()