class TimeMap:

    def __init__(self):
        self.name_to_vts = defaultdict(list) # name : (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.name_to_vts[key].append((value, timestamp)) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.name_to_vts:
            return ""

        vals_timestamps = self.name_to_vts[key]
        l, r = 0, len(vals_timestamps) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2

            if vals_timestamps[m][1] <= timestamp:
                res = vals_timestamps[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res