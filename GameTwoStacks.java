// https://www.hackerrank.com/challenges/game-of-two-stacks

import java.io.*;
import java.util.*;
import java.text.*;

public class GameTwoStacks {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int g = in.nextInt();
        for(int a0 = 0; a0 < g; a0++){
            int n = in.nextInt();
            int m = in.nextInt();
            int x = in.nextInt();
            int[] a = new int[n];
            for(int a_i=0; a_i < n; a_i++){
                a[a_i] = in.nextInt();
            }
            int[] b = new int[m];
            for(int b_i=0; b_i < m; b_i++){
                b[b_i] = in.nextInt();
            }
            // your code goes here
            int a_top = 0, b_top = 0, score = 0, sum = 0;
            
            // first stack
            while (a_top < a.length && sum + a[a_top] <= x)
                sum += a[a_top++];
            score = a_top;
            
            while (b_top < b.length && a_top >= 0) {
                sum += b[b_top++];
                while (sum > x && a_top > 0)
                    sum -= a[--a_top];
                if (a_top + b_top > score && sum <= x)
                    score = b_top + a_top;
            }
            System.out.println(score);
        }
    }
}
