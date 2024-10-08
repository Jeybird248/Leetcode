class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        # Move the accessed key to the end to mark it as recently used
        value = self.map.pop(key)
        self.map[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # Remove the existing key to update its position later
            self.map.pop(key)
        elif len(self.map) >= self.cap:
            # Remove the least recently used key (the first key)
            del self.map[list(self.map.keys())[0]]
        # Insert the new key-value pair, placing it at the end
        self.map[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)