# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        #t = 0
        def check(node, t):
            if len(ans) == t:
                ans.append([])
            ans[t].append(node.val)
            if node.left:
                check(node.left, t+1)
            if node.right:
                check(node.right, t+1)
        check(root, 0)
        return ans
