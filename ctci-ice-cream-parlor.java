// https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int m = in.nextInt();
            int n = in.nextInt();
            int a[] = new int[n];
            HashMap <Integer, Integer> map = new HashMap<Integer, Integer>();
            for(int a_i=0; a_i < n; a_i++){
                a[a_i] = in.nextInt();
                map.put(a[a_i], map.getOrDefault(a[a_i], 0) + 1);
                int diff = m - a[a_i];
                if (map.containsKey(diff)) {
                    int j = n;
                    if (diff == a[a_i]) {
                        if (map.get(diff) > 1) {
                            for (j = 0; j < n;j++) {
                                if (j == a_i)
                                    continue;
                                else if (diff == a[j])
                                    break;
                            }
                        }
                    }
                    else {
                        for (j=0;j < n;j++)
                            if (a[j] == diff)
                                break;
                    }
                    
                    if (j < n) {
                        int f = a_i + 1;
                        int s = j + 1;
                        if (f > s) {
                            int _t = f;
                            f = s;
                            s = _t;
                        }
                        System.out.println(f + " " + s);
                    }
                }
            }
        }
    }
}
