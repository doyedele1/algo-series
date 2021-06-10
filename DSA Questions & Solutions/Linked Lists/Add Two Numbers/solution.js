/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummyNode = new ListNode(0);
    let temp = dummyNode;
    let carry = 0;
    let sum = 0;
    
    // 342
    // 465
    while(l1 || l2) {
        sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry;
        
        if(sum > 9) {
            sum -= 10;
            carry = 1;
        } else carry = 0;
        
        temp.next = new ListNode(sum)
        temp = temp.next
        l1 = l1?.next
        l2 = l2?.next
    }
    
    if(carry === 1) {
        temp.next = new ListNode(carry)
    }
    
    return dummyNode.next
};
    
     // 9  9  9  9  9  9  9
     // 9  9  9  9
     // 8  9  9  9  0  0  0   1