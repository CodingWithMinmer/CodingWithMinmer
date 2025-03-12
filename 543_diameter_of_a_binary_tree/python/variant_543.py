from typing import Optional, List

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def longest_path(node: 'Node'):
            if node is None:
                return 0

            max_height = 0
            second_max_height = 0
            for child in node.children:
                height = longest_path(child)
                if height > max_height:
                    second_max_height = max_height
                    max_height = height
                elif height > second_max_height:
                    second_max_height = height
            nonlocal diameter
            diameter = max(diameter, max_height + second_max_height)
            return max_height + 1

        longest_path(root)

        return diameter