/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */

var deleteNode = function(node) {
    node.val = node.next.val // 5 = 1
    node.next = node.next.next // 2nd 1 = 9
};


// 4 --> 5 --> 1 --> 9

//  next node of 4 = previous next next node of 4
// 4 --> 1 --> 1 --> 9

// 4 --> 1 --> 9