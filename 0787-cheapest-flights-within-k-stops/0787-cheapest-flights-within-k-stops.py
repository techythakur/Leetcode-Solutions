class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for s,e,p in flights:
            graph[s][e] = p
        cost = [math.inf for _ in range(n)]
        q = deque([[src, 0]])
        for _ in range(k+1):
            size = len(q)
            for _ in range(size):
                [ele, curCost] = q.popleft()
                for nextNode in graph[ele]:
                    nextNodePrice = curCost+graph[ele][nextNode]
                    if nextNodePrice<cost[nextNode]:
                        cost[nextNode] = nextNodePrice
                        q.append([nextNode, nextNodePrice])
        if cost[dst]==math.inf:
            return -1
        return cost[dst]
