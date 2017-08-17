// https://www.hackerrank.com/challenges/ctci-balanced-brackets

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    private static final Map<Character, Character> brackets = Collections.unmodifiableMap(
        new HashMap<Character, Character>(){{
            put(')','(');
            put(']','[');
            put('}','{');
        }});
    
    public static boolean isBalanced(String expression) {
        Stack<Character> stack = new Stack<Character>();
        int i = 0;
        while (i < expression.length()) {
            if (brackets.containsKey(expression.charAt(i))) {
                if (stack.empty() || stack.pop() != brackets.get(expression.charAt(i)))
                    break; // unbalanced
            }
            else
                stack.push(expression.charAt(i));
            i++;
        }
        return (i == expression.length()) && stack.empty();
    }
  
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
            System.out.println( (isBalanced(expression)) ? "YES" : "NO" );
        }
    }
}
