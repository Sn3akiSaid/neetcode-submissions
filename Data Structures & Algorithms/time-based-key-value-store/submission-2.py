class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Now we've ensured there's an empty list for that key
        # So we can just append to end of list the value and timestamp
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns the most recent value for key not exceeding the given timestamp, (prev_timestamp <= timestamp).
        """
        res = ""

        values = self.store.get(key, [])

        # Binary search

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            # We are not looking for a bigger timestamp, so don't update res
            else:
                r = mid - 1
        return res