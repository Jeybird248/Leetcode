class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.history = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.history.remove(key)
            self.history.append(key)
        return self.d.get(key, -1)

    def put(self, key: int, value: int) -> None:
        
        if key in self.d:
            self.history.remove(key)
            self.history.append(key)
            self.d[key] = value
        else:
            if len(self.d) >= self.cap:
                while True:
                    temp =  self.history.pop(0)
                    if temp in self.d:
                        self.d.pop(temp)
                        break
            self.d[key] = value
            self.history.append(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)