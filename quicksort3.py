"""
Lomuto Parition: https://www.hackerrank.com/challenges/quicksort3
"""

def print_array(arr):
    print(" ".join(map(str, arr)))

def partition(arr, l, r):
    i = l - 1
    for j in range(l, r+1):
        if arr[j] <= arr[r]:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
    return i

# l and r inclusive indices
def quicksort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        print_array(arr) # print after partition
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, r)

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    quicksort(arr, 0, n-1)

if __name__ == '__main__':
    main()
