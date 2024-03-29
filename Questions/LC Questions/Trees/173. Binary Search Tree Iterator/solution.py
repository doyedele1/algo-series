# Definition for a binary tree node.
from typing import Optional

''' FIRST SOLUTION
        Explanation:
            - Take all the values in inorder fashion into a list and iterate over the list and return what is at that index
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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        # making use of an array to flatten the BST
        self.arr = []
        
        # an iterator or pointer to be used on the sorted array
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
        


''' MOST OPTIMAL SOLUTION
        Explanation:
            - We will use stack. Start pushing all left values into the stack
            - When the next function is called, we pop the top of the stack and check if there is a right child. We call partial inorder on its right child
                        
            TC - O(1) for both next and hasNext methods
            SC - O(h) where h is the height of the BST
'''
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.partialInorder(root)
        
    def partialInorder(self, root):
        while root != None:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        top = self.stack.pop()
        self.partialInorder(top.right)
        return top.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()