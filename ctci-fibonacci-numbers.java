// https://www.hackerrank.com/challenges/ctci-fibonacci-numbers

import java.util.*;

public class Solution {

    public static int fibonacci(int n) {
        if (n < 2)
            return n;
        int prev = 0, curr = 1;
        for (int i = 2; i <= n; i++) {
            int temp = curr + prev;
            prev = curr;
            curr = temp;
        }
        return curr;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        System.out.println(fibonacci(n));
    }
}
