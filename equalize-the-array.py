"""
https://www.hackerrank.com/challenges/equality-in-a-array
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    n = int(raw_input().strip())
    array = map(int, raw_input().strip().split())
    count = [0 for _ in xrange(100)] #count array
    for number in array:
        count[number - 1] += 1
    print len(array) - max(count)

if __name__ == '__main__':
    main()
