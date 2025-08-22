from collections import deque
from customObject import CustomNestedInteger
from typing import  List,Union
import unittest
# VARIANT: What if you had to define your own schema for NestedList and implement BFS?


class SolutionDFS:
    def depthSum(self, objs: List[CustomNestedInteger]) -> int:
        queue = deque(objs)
        level = 1
        sum = 0
        while queue:
            for _ in range(len(queue)):
                obj = queue.popleft()
                if isinstance(obj.value, int):
                    sum += obj.value * level
                else:
                    queue.extend(obj.value)
            level += 1

        return sum
    


# --- Unit Tests ---
class TestNestedWeightListSum(unittest.TestCase):

    def _create_nested_list_from_raw(self, data: List[Union[int, list]]) -> List[CustomNestedInteger]:
        nested_objects = []
        for item in data:
            if isinstance(item, int):
                nested_objects.append(CustomNestedInteger(item))
            elif isinstance(item, list):
                # Recursively create nested lists for nested structures
                nested_objects.append(CustomNestedInteger(self._create_nested_list_from_raw(item)))
            else:
                # If it's already a CustomNestedInteger, just append it
                nested_objects.append(item)
        return nested_objects

    # --- Tests for SolutionDFS (your current BFS implementation) ---

    def test_dfs_single_element(self):
        obj1 = CustomNestedInteger(100)
        s = SolutionDFS()
        objs = [obj1]
        self.assertEqual(100, s.depthSum(objs))

    def test_dfs_flat_list(self):
        root_list = self._create_nested_list_from_raw([1, 2, 3, 4, 5])
        s = SolutionDFS()
        self.assertEqual(15, s.depthSum(root_list))

    def test_dfs_nested(self):
        # Building the nested structure using the helper for readability
        # [1, [2, [3, [4]]]]
        nested_structure = self._create_nested_list_from_raw([
            1, 
            [2, 
                [3, 
                    [4]
                ]
            ]
        ])
        s = SolutionDFS()
        # The input to depthSum should be a list of CustomNestedInteger objects at the current level.
        # Here, the top-level list has only one element which contains the full structure.
        self.assertEqual(30, s.depthSum(nested_structure))

    def test_dfs_complex(self):
        # [8, 4, [5, [9], 3], 6]
        complex_list = self._create_nested_list_from_raw([
            8, 4, 
            [5, [9], 3], 
            6
        ])
        s = SolutionDFS()
        self.assertEqual(61, s.depthSum(complex_list))

        # [4, 2, [[9]], -3]
        complex_list_2 = self._create_nested_list_from_raw([
            4, 2, 
            [[9]], 
            -3
        ])
        self.assertEqual(30, s.depthSum(complex_list_2))

    def test_dfs_negatives(self):
        # [8, 4, [5, [-9], 3], -6]
        negatives_list = self._create_nested_list_from_raw([
            8, 4, 
            [5, [-9], 3], 
            -6
        ])
        s = SolutionDFS()
        self.assertEqual(-5, s.depthSum(negatives_list))

    def test_dfs_all_zeroes(self):
        # [0, 0, [0, [0], 0], 0]
        zeroes_list = self._create_nested_list_from_raw([
            0, 0, 
            [0, [0], 0], 
            0
        ])
        s = SolutionDFS()
        self.assertEqual(0, s.depthSum(zeroes_list))
    

   
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

