'''
    Explanation:
        TC: 
            - Serialization: O(N)
            - Deserialization: O(N)
        SC:
            - Serialization: O(N) - Recursion stack and the result string
            - Deserialization: O(N) - Recursion stack and the queue
'''

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root: 'Node') -> str:
        """
            Encodes a tree to a single string.
            
            :type root: Node
            :rtype: str
        """

        def serializeHelper(node):
            if not node:
                self.res += 'None,'
                return
            
            self.res += str(node.val) + "#"
            self.res += str(len(node.children)) + ","
            for child in node.children:
                serializeHelper(child)
            
        if not root: return ""
        self.res = ""
        serializeHelper(root)
        return self.res[:-1] #[:-1] removes the final comma
	
    def deserialize(self, data: str) -> 'Node':
        """
            Decodes your encoded data to tree.
            
            :type data: str
            :rtype: Node
        """

        def deserializeHelper():
            if not q: return None

            data = q.popleft()
            nodeVal, numOfChildren = data.split("#")

            node = Node(int(nodeVal))
            node.children = []

            for i in range(int(numOfChildren)):
                node.children.append(deserializeHelper())
            return node

        if not data: return None
        q = deque(data.split(","))
        return deserializeHelper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))