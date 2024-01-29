class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        dic = {}
        stack = []
        for i in range(len(rooms)):
            dic[i] = rooms[i]
        for i in dic[0]:
            stack.append(i)
        visited.add(0)
        
        while len(stack) > 0:
            curr = stack.pop()
            visited.add(curr)
            for i in dic[curr]:
                if i not in visited:
                    stack.append(i)
        
        return len(dic) == len(visited)