'''
    Explanation:
        serialize()
            Perform preorder traversal to serialize the binary tree
                                1
                   2                                3
            None       None                4                 5
                                    None       None   None       None
            res = "1, 2, None, None, 3, 4, None, None, 5, None, None,". res has a delimeter of ","

        TC: O(N) for both serialize and deserialize functions
        SC: O(N) for both functions for the recursive call stack
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """
            Encodes a tree to a single string.
            
            :type root: TreeNode
            :rtype: str
        """
        
        def serializeHelper(node):
            if not node:
                self.res += "None,"
                return
            
            self.res += str(node.val) + ","
            serializeHelper(node.left)
            serializeHelper(node.right)
    
        self.res = ""
        serializeHelper(root)
        return self.res[:-1]

    def deserialize(self, data):
        """
            Decodes your encoded data to tree.
            
            :type data: str
            :rtype: TreeNode
        """

        def deserializeHelper():
            if not q: return None
            if q[0] == "None":
                q.popleft()
                return None

            node = TreeNode(int(q[0]))
            q.popleft()
            node.left = deserializeHelper()
            node.right = deserializeHelper()

            return node
        
        q = deque(data.split(","))
        return deserializeHelper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))