// https://www.hackerrank.com/challenges/cut-the-tree/

import java.io.*;
import java.util.*;

public class Solution {

    // sum of subtree rooted at root
    static int subTreeSum(int n, int data[],
                            ArrayList<ArrayList<Integer>>edges, int root,
                            int[]subSum, int visited[])
    {
        if (visited[root] == 1)
            return 0;
        
        visited[root] = 1;  // mark visited
        int sum = data[root];
        for (Integer node: edges.get(root))
            sum += subTreeSum(n, data, edges, node.intValue(), subSum, visited);
        subSum[root] = sum;
        return subSum[root];
    }
    
    // sum of subtrees rooted at all nodes
    static int[] subTreeSum(int n, int data[], ArrayList<ArrayList<Integer>>edges) {
        int subSum[] = new int[n];
        int visited[] = new int[n];
        subTreeSum(n, data, edges, 0, subSum, visited);
        return subSum;
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int data[] = new int[n];
        ArrayList<ArrayList<Integer>>edges = new ArrayList<ArrayList<Integer>>(n);
        for (int i = 0; i < n; i++) {
            data[i] = in.nextInt();
            edges.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < n-1; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            edges.get(a-1).add(b-1);
            edges.get(b-1).add(a-1);
        }
        in.close();
        
        int[] subSum = subTreeSum(n, data, edges);
        int total = subSum[0];      // total sum of the tree
        int minDiff = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++) {
            int diff = Math.abs(total - 2*subSum[i]);   // abs diff of two subtrees
            minDiff = Math.min(minDiff, diff);
        }
        System.out.println(minDiff);
    }
}