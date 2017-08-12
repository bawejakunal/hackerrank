// https://www.hackerrank.com/challenges/game-with-cells

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        in.close();
        int total = (int)(Math.ceil(n/2.0) * Math.ceil(m/2.0));  // 1 supply to 4 cells greedy strategy
        System.out.println(total);
    }
}
