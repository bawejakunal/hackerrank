/**
 *
 * https://www.hackerrank.com/challenges/swap-nodes-algo
 *
 **/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Node {
    int left = -1;
    int right = -1;
    
    void swapSubtrees() {
        int temp = this.left;
        this.left = this.right;
        this.right = temp;
    }
}

public class SwapNodesAlgo {

    private static void inOrder(Node arr[], int root) {
        if (root == -1)
            return;
        inOrder(arr, arr[root].left);
        System.out.print((root + 1) + " "); // 0 based indices
        inOrder(arr, arr[root].right);
    }
    
    
    private static void preOrderSwap(Node arr[], int root, int depth, int K) {
        if (root == -1)
            return;
        
        if (depth % K == 0)
            arr[root].swapSubtrees();
        
        preOrderSwap(arr, arr[root].left, depth + 1, K);
        preOrderSwap(arr, arr[root].right, depth + 1, K);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T, K, d;
        int N = in.nextInt();
        Node tree[] = new Node[N];
        
        for (int i = 0; i < N; i++) {
            tree[i] = new Node();
            tree[i].left = in.nextInt();
            tree[i].right = in.nextInt();
            
            // 0 based indices
            tree[i].left = tree[i].left > 0 ? tree[i].left - 1: tree[i].left;
            tree[i].right = tree[i].right > 0 ? tree[i].right - 1: tree[i].right;
        }
        
        T = in.nextInt();
        while (T-- > 0) {
            K = in.nextInt();
            preOrderSwap(tree, 0, 1, K);
            inOrder(tree, 0); 
            System.out.println();
        }
    }
}
