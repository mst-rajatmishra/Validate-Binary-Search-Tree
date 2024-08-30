class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return (is_valid(node.left, min_val, node.val) and
                    is_valid(node.right, node.val, max_val))
        
        # Initialize the recursion with extreme values
        return is_valid(root, float('-inf'), float('inf'))

# Example usage:
solution = Solution()
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(solution.isValidBST(root1))  # Output: True

root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(solution.isValidBST(root2))  # Output: False
