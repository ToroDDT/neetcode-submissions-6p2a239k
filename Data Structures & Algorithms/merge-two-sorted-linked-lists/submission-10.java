/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Base cases: if one list is empty, return the other
        if (list1 == null) return list2;
        if (list2 == null) return list1;

        if (list1.val <= list2.val) {
            // list1 is smaller, so it comes first.
            // Its next element is the result of merging the rest.
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            // list2 is smaller.
            // Its next element is the result of merging the rest.
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
}