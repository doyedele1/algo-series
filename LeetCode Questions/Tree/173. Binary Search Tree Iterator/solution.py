# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        # making use of an array to flatten the BST
        self.arr = []
        
        #an iterator or pointer to be used on the sorted array
        self.index = -1
        
        # flattening the BST in an inorder fashion
        self.inorder(root)
        
    def inorder(self, root):
        if root == None:
            return []

        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
        
    def next(self) -> int:
        self.index += 1
        return self.arr[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.arr)
        
        
    '''
        Explanation:
            Time Complexity: 
                For initializing the new object of the class- O(n) where n is the number of nodes in the BST
                For calling the function next() - O(1)
                For calling the function hasNext() - O(1)

            Space Complexity:
                For initializing the new object of the class- O(n) since we created a new array to store all the nodes in the BST
                For calling the function next() - O(n) since the new array is used
                For calling the function hasNext() - O(n) since the new array is used
                If the BST is balanced, the space complexity is O(h) where h is the height of the BST and the height of a balanced BST is log(n)
    '''
    
    


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()