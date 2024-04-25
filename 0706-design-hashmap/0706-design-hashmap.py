class MyHashMap:

    def __init__(self):
        self.s=defaultdict(int)

    def put(self, key: int, value: int) -> None:
        self.s[key]=value

    def get(self, key: int) -> int:
        # print(self.s.get(key), self.s)
        return self.s.get(key) if (self.s.get(key) is not None)  else -1
    
    def remove(self, key: int) -> None:
        self.s[key]=None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)