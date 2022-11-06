# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def serializeHelper(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))

            serializeHelper(node.left)
            serializeHelper(node.right)
        
        serializeHelper(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.progress = 0

        def deserializeHelper():
            if vals[self.progress] == "N":
                self.progress += 1
                return None

            node = TreeNode(int(vals[self.progress]))
            self.progress += 1
            node.left = deserializeHelper()
            node.right = deserializeHelper()
            return node
        return deserializeHelper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))