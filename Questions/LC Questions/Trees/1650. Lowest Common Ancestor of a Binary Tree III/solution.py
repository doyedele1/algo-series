# Definition for a Node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

'''
    Follow up questions to ask the interviewer --> 
    1. Are all Node values unique?
    2. Can Node p be not equal to Node q?
    3. Can both Nodes p and q not exist in the tree?
'''

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        current_p = p
        current_q = q
        
        while current_p != current_q:
            if current_p.parent == None:
                current_p = q
            else: current_p = current_p.parent
            if current_q.parent == None:
                current_q = p
            else: current_q = current_q.parent
        return current_p