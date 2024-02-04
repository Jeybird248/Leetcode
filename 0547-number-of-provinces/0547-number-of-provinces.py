class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node, visited):
            visited.add(node)  # Mark the current node as visited
            for neighbor, connection in enumerate(isConnected[node]):
                if neighbor not in visited and connection:
                    dfs(neighbor, visited)  # Recursively visit unvisited neighbors

        num_provinces = 0  # Initialize the count of provinces
        visited_nodes = set()  # Set to keep track of visited nodes

        # Iterate through each node in the graph
        for node in range(len(isConnected)):
            if node not in visited_nodes:
                num_provinces += 1  # Found a new province
                dfs(node, visited_nodes)  # Explore the province

        return num_provinces
