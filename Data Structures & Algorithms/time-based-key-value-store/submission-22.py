class TimeMap:

    def __init__(self):
        self.key_to_val = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_val[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_val:
            return ""

        vals = self.key_to_val[key]
        l, r = 0, len(vals) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2
            ts, val = vals[m]

            if ts == timestamp:
                return val
            
            if ts < timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1
                
        return res
            
