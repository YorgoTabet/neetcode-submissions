class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        // Ensure fast and fast.next are not null before jumping two steps
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            // Check if they meet after moving
            if (slow == fast) {
                return true;
            }
        }

        // If fast reaches the end of the list, there is no cycle
        return false;
    }
}
