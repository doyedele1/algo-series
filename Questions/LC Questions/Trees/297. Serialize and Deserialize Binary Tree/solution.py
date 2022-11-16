'''
    Explanation:
        - serialize()
            Perform preorder traversal to serialize the binary tree
                                1
                2                           3
            X       X                   4           5
                                    X       X   X       X
            res = "1, 2, X, X, 3, 4, 5, X, X, X, X". res has a delimeter of ","

        - deserialize()
            - Split the res encoded string into an array of strings
            - Perform preorder traversal to construct the tree
            - Keep track of the index you are on your splitted data

        - TC: O(n) for both serialize and deserialize functions
        - SC: O(n) for both functions for the recursive call stack
'''


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
        
        res = []

        def serializeHelper(node):
            if not node:
                res.append("X")
                return

            res.append(str(node.val))

            serializeHelper(node.left)
            serializeHelper(node.right)
        
        serializeHelper(root)
        return ",".join(res)

    def deserialize(self, data):
        """
            Decodes your encoded data to tree.
            
            :type data: str
            :rtype: TreeNode
        """

        values = data.split(",")
        self.progress = 0

        def deserializeHelper():
            if values[self.progress] == "X":
                self.progress += 1
                return None

            node = TreeNode(int(values[self.progress]))
            self.progress += 1
            node.left = deserializeHelper()
            node.right = deserializeHelper()
            
            return node
        return deserializeHelper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))