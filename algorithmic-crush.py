"""
https://www.hackerrank.com/challenges/crush

Hint: at bottom
"""


def main():
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(M):
        a, b, k = map(int, input().split())
        arr[a-1] += k
        if b < N:
            arr[b] -= k

    maximum = x = 0
    for num in arr:
        x += num
        if x > maximum:
            maximum = x
    print(maximum)

if __name__ == '__main__':
    main()

"""
Instead of storing the actual values in the array, you store the difference
between the current element and the previous element. So you add k to arr[a-1]
showing that arr[a-1] is greater than its previous element by k. You subtract
k from arr[b] to show that arr[b] is less than arr[b-1] by k. By the end of
all this, you have an array that shows the difference between every successive
element. By adding all the positive differences, you get the value of the
maximum element
"""