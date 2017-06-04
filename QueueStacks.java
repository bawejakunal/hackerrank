/**
 *
 * https://www.hackerrank.com/challenges/queue-using-two-stacks/
 *
 **/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Queue{
    private ArrayDeque <Integer> stack1 = new ArrayDeque <Integer> ();
    private ArrayDeque <Integer> stack2 = new ArrayDeque <Integer> ();
    
    boolean isEmpty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }
    
    void enqueue(Integer element) {
        stack1.push(element);
    }
    
    Integer dequeue() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty())
                stack2.push(stack1.pop());
        }
        return stack2.pop();
    }
    
    Integer element() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty())
                stack2.push(stack1.pop());
        }
        return stack2.peek();
    }
}

public class QueueStacks {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Queue queue = new Queue();
        int q, t, x;
        q = in.nextInt();
        while(q-- > 0) {
            t = in.nextInt();
            switch(t) {
                case 1: x = in.nextInt();
                        queue.enqueue(new Integer(x));
                        break;
                case 2: queue.dequeue();
                        break;
                case 3: System.out.println(queue.element());
                        break;
            }
        }
    }
}
