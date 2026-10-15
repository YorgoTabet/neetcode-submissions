class TimeMap:
    def __init__(self):
        self.map = defaultdict(list[tuple[int, str]])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val = self.map.get(key, [])
        if len(val):
            l, r = 0, len(val) - 1
            prev = ""
            while l <= r:
                mid = (l + r) // 2

                if timestamp == val[mid][0]:
                    return val[mid][1]

                if timestamp < val[mid][0]:
                    r = mid - 1
                else:
                    prev = val[mid][1]
                    l = mid + 1
            
            return prev
        return ""
