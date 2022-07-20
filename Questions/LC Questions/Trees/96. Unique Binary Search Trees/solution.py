class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
            
        numTree = [0] * (n + 1)
        numTree[0] = 1
        numTree[1] = 1
        numTree[2] = 2
        numTree[3] = 5
        for i in range(4, n + 1):
            for j in range(1, i + 1):
                numTree[i] += numTree[j - 1] * numTree[i - j]
            print(numTree)
        return numTree[n]
    
    
    # Explanation - n = 4
    # numTree[4] = numTree[0] * numTree[3] + numTree[1] * numTree[2] + numTree[2] * numTree[1] + numTree[3] * numTree[0]
    
    # TC - O(n-squared)
    # SC - O(n)



# kth largest element solution
# class Solution:
#     def kthLargest(self, root: TreeNode, k: int) -> int:
#         self.k = k
#         self.res = None
#         self.helper(root)
#         return self.res

#     def helper(self, root):
#         if not root:
#             return
#         self.helper(root.right)
#         self.k -= 1
#         if self.k == 0:
#             self.res = root.val
#             return
#         self.helper(root.left)


# # kth smallest element solution
# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         self.k = k
#         self.res = None
#         self.helper(root)
#         return self.res

#     def helper(self, root):
#         if not root:
#             return
#         self.helper(root.left)
#         self.k -= 1
#         if self.k == 0:
#             self.res = root.val
#             return
#         self.helper(root.right)
