// https://www.hackerrank.com/challenges/ctci-linked-list-cycle

/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.
https://news.vice.com/story/vice-news-tonight-full-episode-charlottesville-race-and-terror
A Node is defined as: 
    class Node {
        int data;
        Node next;
    }
*/

boolean hasCycle(Node head) {
    Node slow = head, fast = head;
    while (fast != null && fast.next != null && slow != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast)
            return true;
    }
    return false;
}
