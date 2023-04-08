"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(vertex):
            if not vertex:
                return vertex
            #blocking cycle infinite
            if vertex in visited:
                return visited[vertex] 
            clone_node = Node(vertex.val, [])
            visited[vertex]=clone_node
            if vertex.neighbors:
                clone_node.neighbors = [dfs(n) for n in vertex.neighbors] 
            return clone_node  
        visited={}
        return dfs(node)