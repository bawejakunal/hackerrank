// https://www.hackerrank.com/challenges/special-multiple/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        while (T-- > 0) {
            int n = in.nextInt();
            long j = 1;
            String bin = Long.toBinaryString(j);
            while ((Long.parseLong(bin.replace('1', '9')) % n) != 0) {
                j++;
                bin = Long.toBinaryString(j);
            }
            System.out.println(bin.replace('1', '9'));
        }
        in.close();
    }
}