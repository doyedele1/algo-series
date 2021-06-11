/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if(root === null) {
        return root;
    }
    
    if(root) {
        // traverse through the tree
        var leftRoot = invertTree(root.left);
        var rightRoot = invertTree(root.right);
        
        // swap
        root.left = rightRoot;
        root.right = leftRoot;

        return root;
    }
};