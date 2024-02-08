class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.arr = []

        def dfs(graph, curr, currList):
            currList = currList.copy()

            if curr == len(graph) - 1:
                self.arr.append(currList)
            else:
                for subgraph in graph[curr]:
                    currList.append(subgraph)
                    dfs(graph, subgraph, currList)
                    currList.pop()

        dfs(graph, 0, [0])
        return self.arr