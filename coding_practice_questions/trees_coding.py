#Pre-order traversal
#####################################################################################################################################
# https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/

#SOlution 1: Iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            stack=[root]
            res=[]
            while len(stack)!=0:
                node=stack.pop()
                res.append(node.val)
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
            return res
        else:
            return []

#Solution 2: Recursive 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res    
        
#In-order traversal
#####################################################################################################################################
# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
# Solution 1: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        return self.res



#SOlution 2: Iterative


# Post-order traversal
#####################################################################################################################################
#https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/

# Solution 1: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        return self.res

#SOlution 2: Iterative





# Level order traversal
#####################################################################################################################################


# Lowest Common Ancestor of a Binary Tree
#####################################################################################################################################
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Binary Tree Maximum Path Sum
#####################################################################################################################################
# https://leetcode.com/problems/binary-tree-maximum-path-sum

# Binary Tree Right Side View
#####################################################################################################################################
# https://leetcode.com/problems/binary-tree-right-side-view

# Serialize and Deserialize Binary Tree
#####################################################################################################################################
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# All Nodes Distance K in Binary Tree
#####################################################################################################################################
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

# Count Good Nodes in Binary Tree
#####################################################################################################################################
# https://leetcode.com/problems/count-good-nodes-in-binary-tree


# Lowest Common Ancestor of a Binary Tree III
#####################################################################################################################################
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii

# Validate Binary Search Tree
#####################################################################################################################################
# https://leetcode.com/problems/validate-binary-search-tree


# Vertical Order Traversal of a Binary Tree
#####################################################################################################################################
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# Convert Binary Search Tree to Sorted Doubly Linked List
#####################################################################################################################################
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list

# Diameter of Binary Tree
#####################################################################################################################################
# https://leetcode.com/problems/diameter-of-binary-tree


# Binary Tree Zigzag Level Order Traversal
#####################################################################################################################################
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Invert Binary Tree
#####################################################################################################################################
# https://leetcode.com/problems/invert-binary-tree

# Balance a Binary Search Tree
#####################################################################################################################################
# https://leetcode.com/problems/balance-a-binary-search-tree

# Binary Tree Level Order Traversal
#####################################################################################################################################
# https://leetcode.com/problems/binary-tree-level-order-traversal

# Flatten Binary Tree to Linked List
#####################################################################################################################################
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Construct Binary Tree from Preorder and Inorder Traversal
#####################################################################################################################################
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Symmetric Tree
#####################################################################################################################################
# https://leetcode.com/problems/symmetric-tree

# Unique Binary Search Trees
#####################################################################################################################################
# https://leetcode.com/problems/unique-binary-search-trees

# Cousins in Binary Tree
#####################################################################################################################################
# https://leetcode.com/problems/cousins-in-binary-tree


# Construct Binary Search Tree from Preorder Traversal
#####################################################################################################################################
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Inorder Successor in BST
#####################################################################################################################################
# https://leetcode.com/problems/inorder-successor-in-bst
