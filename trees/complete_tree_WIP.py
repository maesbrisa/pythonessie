#!/bin/env python

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def compute_depth(node):
    d = 0
    while node.left:
        node = node.left
        d += 1
    return d

def exists(idx, d, node):
    left, right = 0, 2**d-1
    for _ in range(d): # ignore index
        pivot = left + (right - left)//2 # return no decimals
        if idx <= pivot:
            node = node.left
            right = pivot
        else:
            node = node.right
            left = pivot + 1
    return node is not None

def countNodes(root):
    if not root:
        return 0
    d = compute_depth(root)
    if d == 0:
        return 1
    # binary search
    left, right = 1, 2**d-1
    while left <= right:
        pivot = left + (right - left) // 2
        print(pivot)
        if exists(pivot, d, root):
            left = pivot + 1
        else:
            right = pivot + 1
    return (2**d-1)+left

if __name__ == '__main__':
    c_12 = TreeNode(12)
    c_11 = TreeNode(11)
    c_10 = TreeNode(10)
    c_9 = TreeNode(9)
    c_8 = TreeNode(8)
    c_7 = TreeNode(7)
    c_6 = TreeNode(6, c_12)
    c_5 = TreeNode(5, c_10, c_11)
    c_4 = TreeNode(4, c_8, c_9)
    c_3 = TreeNode(3, c_6, c_7)
    c_2 = TreeNode(2, c_4, c_5)
    root = TreeNode(1, c_2, c_3)

    print(countNodes(root))
