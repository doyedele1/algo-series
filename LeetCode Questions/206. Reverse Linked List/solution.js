
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// Iterative solution - O(n) time, O(1) space
var reverseList = function(head) {
    let previous = None
    let current = head
        
    while(current != null) {
        next = current.next
        current.next = previous
        previous = current
        current = next
    }

    return previous
};

// Recursive solution - O(n) time, O(n) space
var reverseList = function(head) {
    if(head === null || head.next === null) {
        return head
    }

    var reversedList = reverseList(head.next)
    head.next.next = head
    head.next = null
    return reversedList
};