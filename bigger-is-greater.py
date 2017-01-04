"""
https://www.hackerrank.com/challenges/bigger-is-greater

https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""

def main():
    """
    Lexicographical permutation algorithm
    """
    t = int(raw_input().strip())
    while t > 0:
        t -= 1
        word = list(raw_input().strip())
        pivot = -1
        for i in xrange(len(word)-1):
            if word[i] < word[i + 1]:
                pivot = i #last index of prefix, suffix is strictly non-increasing

        if pivot == -1:
            print 'no answer'
            continue

        end = -1
        for i in xrange(pivot+1, len(word)):
            if word[i] > word[pivot]:
                end = i

        word[pivot], word[end] = word[end], word[pivot]
        #reverse the suffix to get sorted order of alphabets
        #this ensures the next lexicographically larger string
        word = word[:pivot+1] + word[pivot+1:][::-1]
        print "".join(word)

if __name__ == '__main__':
    main()
