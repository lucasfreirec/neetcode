"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        myMap = {}

        def cloneNode(n):
            if n.val in myMap:
                return myMap[n.val]

            clone = Node(n.val)

            myMap[clone.val] = clone

            for nei in n.neighbors:
                clone.neighbors.append(cloneNode(nei))

            return clone

        return None if node is None else cloneNode(node)


        
            

        
            
        