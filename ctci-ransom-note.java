// https://www.hackerrank.com/challenges/ctci-ransom-note

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        int n = in.nextInt();
        HashMap<String, Integer> magazine = new HashMap<String, Integer>();
        for(int magazine_i=0; magazine_i < m; magazine_i++){
            String word = in.next();
            if (magazine.containsKey(word))
                magazine.put(word, magazine.get(word) + 1);
            else
                magazine.put(word, 1);
        }
        int ransom_i = 0;
        for(ransom_i=0; ransom_i < n; ransom_i++){
            String word = in.next();
            if (!magazine.containsKey(word) || magazine.get(word) < 1)
                break;
            else
                magazine.put(word, magazine.get(word) - 1);
        }
        System.out.println(ransom_i == n ? "Yes": "No");
    }
}
