from collections import deque
import unittest
from typing import  List,Union
from customObject import CustomNestedInteger


# VARIANT: What if you had to define your own schema for NestedList and implement DFS?
class SolutionBFS:
    def depthSum(self, objs: List[CustomNestedInteger]) -> int:
        def bfs(objs):
            q = deque(objs)
            total = 0
            depth = 1
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    
                    if isinstance(cur.value,int):
                        total += cur.value * depth
                    else:
                        q.extend(cur.value)
                depth +=1
            return total
        return bfs(objs)
        
    
class TestNestedWeightListSum(unittest.TestCase):

    # Helper function to create CustomNestedInteger lists from simpler Python lists/ints
    # This simplifies test case creation significantly.
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

    # --- Tests for SolutionBFS (conceptual DFS implementation) ---

    def test_bfs_single_element(self):
        obj1 = CustomNestedInteger(100)
        s = SolutionBFS()
        objs = [obj1]
        self.assertEqual(100, s.depthSum(objs))

    def test_bfs_flat_list(self):
        root_list = self._create_nested_list_from_raw([1, 2, 3, 4, 5])
        s = SolutionBFS()
        self.assertEqual(15, s.depthSum(root_list))

    def test_bfs_nested(self):
        nested_structure = self._create_nested_list_from_raw([
            1, 
            [2, 
                [3, 
                    [4]
                ]
            ]
        ])
        s = SolutionBFS()
        self.assertEqual(30, s.depthSum(nested_structure))

    def test_bfs_complex(self):
        complex_list = self._create_nested_list_from_raw([
            8, 4, 
            [5, [9], 3], 
            6
        ])
        s = SolutionBFS()
        self.assertEqual(61, s.depthSum(complex_list))

        complex_list_2 = self._create_nested_list_from_raw([
            4, 2, 
            [[9]], 
            -3
        ])
        self.assertEqual(30, s.depthSum(complex_list_2))

    def test_bfs_negatives(self):
        negatives_list = self._create_nested_list_from_raw([
            8, 4, 
            [5, [-9], 3], 
            -6
        ])
        s = SolutionBFS()
        self.assertEqual(-5, s.depthSum(negatives_list))

    def test_bfs_all_zeroes(self):
        zeroes_list = self._create_nested_list_from_raw([
            0, 0, 
            [0, [0], 0], 
            0
        ])
        s = SolutionBFS()
        self.assertEqual(0, s.depthSum(zeroes_list))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
