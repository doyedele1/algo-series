/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    var previous = null;
    var current = head;
    var next = null;
    
    while(current != null) {
        next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    
    return previous;
    
};