// https://www.hackerrank.com/challenges/find-point

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int px = sc.nextInt();
            int py = sc.nextInt();
            int qx = sc.nextInt();
            int qy = sc.nextInt();
            int rx = 2*qx - px;
            int ry = 2*qy - py;
            System.out.format("%d %d\n", rx, ry);
        }
        sc.close();
    }
}