from typing import Optional, List
from utils.N_arryTree import N_arryTree

class Solution:
    def diameter(self, root: 'N_arryTree') -> int:
       
        longetDiameter = 0

        def dfs(node: 'N_arryTree'):
            
            # print(f'cur {node.val}')
            localDiameter = 0
            for child in node.children:

                localDiameter = max(dfs(child),localDiameter)

            
            nonlocal longetDiameter
            longetDiameter = max(longetDiameter,localDiameter+1)
            print(localDiameter,node.val)
            return localDiameter +1

        dfs(root)

        return longetDiameter
    

if __name__ == '__main__':
    root = N_arryTree(1)
    n2 = N_arryTree(2)
    n3 = N_arryTree(3)
    root.children=[n2,n3]

    n4= N_arryTree(4)
    n5= N_arryTree(5)
    n2.children= [n4,n5]

    n6 = N_arryTree(6)
    n7 = N_arryTree(7)
    n8 = N_arryTree(8)
    n9 = N_arryTree(9)
    n5.children =[n6,n7,n8,n9]

    n10 = N_arryTree(10)
    n11 = N_arryTree(11)
    n12 = N_arryTree(12)

    n13 = N_arryTree(13)
    n14 = N_arryTree(14)
    n15 = N_arryTree(15)
    n16 = N_arryTree(16)

    n10.children = [n14]

    n8.children = [n11,n12]
    n9.children = [n13]
    n13.children = [n15]
    n15.children = [n16]

    res = Solution().diameter(root)
    assert res == 7, print(res)

    print('All Test Passed!!!')

