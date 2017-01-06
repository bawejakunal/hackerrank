"""
https://www.hackerrank.com/challenges/almost-sorted
"""

def is_sorted(arr):
    """
    check sorted order
    """
    for i in xrange(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True

def main():
    """
    find longest reversed array
    """
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split())
    left = -1 #starting index
    right = n
    for i in xrange(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            left = i
            break

    #already sorted
    if left == -1:
        print 'yes'
    else:
        for i in xrange(n-1, left, -1):
            if arr[i] < arr[i-1]:
                right = i
                break

        #try swap
        possible = False
        if is_sorted(arr[right:right+1] + arr[left+1:right] + arr[left:left+1]):
            possible = True
            if left > 0 and arr[right] < arr[left - 1]:
                possible = False
            if right < n - 1 and arr[left] > arr[right + 1]:
                possible = False
            
            if possible is True:
                print 'yes'
                print 'swap', left+1, right+1

        if possible is False:
            #try reverse
            if is_sorted(arr[left:right+1][::-1]):
                possible = True
                if left > 0 and arr[right] < arr[left - 1]:
                    possible = False
                if right < n - 1 and arr[left] > arr[right + 1]:
                    possible = False
              
                if possible is True:
                    print 'yes'
                    print 'reverse', left+1, right+1

        if possible is False:
            print 'no'

if __name__ == '__main__':
    main()
