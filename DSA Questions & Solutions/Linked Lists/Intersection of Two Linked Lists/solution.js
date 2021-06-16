/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
 var getIntersectionNode = function(headA, headB) {
    // Using hashmaps
    var seen = new Set();
    
    while(headA != null) {
        seen.add(headA);
        headA = headA.next;
    }
    
    while(headB != null) {
        if(seen.has(headB)) {
            return headB;
        }
        
        headB = headB.next;
    }
    return null;
};