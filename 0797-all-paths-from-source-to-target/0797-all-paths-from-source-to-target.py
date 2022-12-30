class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def dfs(a, path):
            if a == len(graph)-1:
                ans.append(path)
            for neighbour in graph[a]:
                dfs(neighbour,[*path, neighbour])
        dfs(0, [0])
        return ans