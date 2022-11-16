'''
    Explanation:
        TC: O(N) for both serialization and deserialization functions
        SC: O(N) for both serialization and deserialization functions
'''


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """
            Encodes a tree to a single string.
        """

        def serializeHelper(node):
            if not node: return
    
            self.res.append(node.val)
            serializeHelper(node.left)
            serializeHelper(node.right)
        
        self.res = []
        serializeHelper(root)
        return ",".join(map(str, self.res))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
            Decodes your encoded data to tree.
        """

        def deserializeHelper(q, lower, upper):
            if not q: return None
            if not lower <= q[0] <= upper: return None

            node = q.pop(0)
            node = TreeNode(node)
            node.left = deserializeHelper(q, lower, node.val)
            node.right = deserializeHelper(q, node.val, upper)

            return node
        
        if not data: return None
        q = [int(d) for d in data.split(",")]
        return deserializeHelper(q, -float("inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans