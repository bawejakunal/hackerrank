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

def check_index_swap(left, right, arr, n):
    """
    basically swap or reverse operation both effectively
    swap positions of arr[left] and arr[right]. So make
    sure that this swapped order also ensures the overall
    sorted order of arr
    """
    if left > 0 and arr[right] < arr[left - 1]:
        return False
    if right < n - 1 and arr[left] > arr[right + 1]:
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

        possible = check_index_swap(left, right, arr, n)
        if possible is False:
            print 'no'
        else:
            #try swap
            if is_sorted(arr[right:right+1] + arr[left+1:right]
                         + arr[left:left+1]):
                print 'yes'
                print 'swap', left+1, right+1

            #try reverse
            elif is_sorted(arr[left:right+1][::-1]):
                print 'yes'
                print 'reverse', left+1, right+1

            else:
                print 'no'

if __name__ == '__main__':
    main()
