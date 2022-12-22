class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_ls = [[] for _ in range(n)]
        for u, v in edges:
            adj_ls[u].append(v)
            adj_ls[v].append(u)

        num_node = [1] * n
        num_dist = [0] * n
        def dfs0(u, p):
            for v in adj_ls[u]:
                if v != p:
                    dfs0(v, u)
                    num_node[u] += num_node[v]
                    num_dist[u] += num_node[v] + num_dist[v]

        def dfs1(u, p):
            if p != -1:
                num_dist[u] = num_dist[p] - num_node[u] + n - num_node[u]
            for v in adj_ls[u]:
                if v != p:
                    dfs1(v, u)

        dfs0(0, -1)
        dfs1(0, -1)
        return num_dist