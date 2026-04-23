class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list) # { key : (timestamp, value)}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ""

        vs = self.kv_store[key]
        res = ""
        l, r = 0, len(vs) - 1

        while l <= r:
            m = l + (r - l) // 2
            if vs[m][0] == timestamp:
                return vs[m][1]
            
            if vs[m][0] < timestamp:
                res = vs[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res

        
