package linkedlist.day19;

class Solution {
    public void deleteNode(ListNode node) {

                node.val = node.next.val;
                node.next = node.next.next;

 


    }
}
