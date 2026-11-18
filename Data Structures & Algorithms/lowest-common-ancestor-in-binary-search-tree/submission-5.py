# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visited = set()
        tmp = root
        visited.add(root.val)
        LCA = root

        while tmp.val != p.val:    
            if p.val < tmp.val:
                tmp = tmp.left
            else:
                tmp = tmp.right
            
            visited.add(tmp.val)
        
        tmp = root

        while tmp.val != q.val:    
            if q.val < tmp.val:
                tmp = tmp.left
            else:
                tmp = tmp.right
            
            if tmp.val in visited:
                LCA = tmp
        
        return LCA





