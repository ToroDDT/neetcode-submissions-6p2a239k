class Solution {

    public ListNode reverseList(ListNode head) {
        return recursion(head);
    }

    public ListNode recursion(ListNode head) {
        // Base case: empty list or last node
        if (head == null || head.next == null) {
            return head;
        }

        // Reverse the rest of the list
        ListNode newHead = recursion(head.next);

        // Fix the current node
        head.next.next = head;
        head.next = null;

        return newHead;
    }
}