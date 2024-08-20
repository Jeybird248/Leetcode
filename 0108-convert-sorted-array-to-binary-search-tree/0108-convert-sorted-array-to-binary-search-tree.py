# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Choose the Middle Element: The middle element of the array becomes the root of the BST. This splits the array into two halves.

        Recursively Build the Subtrees:

            The left half of the array becomes the left subtree.
            The right half of the array becomes the right subtree.

        Base Case: If the array (or subarray) is empty, return None.
        """
        
        if not nums:
            return None
        middle = (len(nums)) // 2 

        left = nums[:middle]
        right = nums[middle + 1:]

        return TreeNode(nums[middle], self.sortedArrayToBST(left), self.sortedArrayToBST(right))
    