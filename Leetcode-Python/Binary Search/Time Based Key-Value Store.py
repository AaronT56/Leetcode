from collections import defaultdict
class TimeMap:
    # So sometimes for example in stocks, we dont just want to know values but
    # a key (stock name) that corresponds to a value (stock price) at a time (timestamp).
    # So we have to take a given key, and based on this we search 'is this value present
    # for this key' and if not 'is there any present for an earlier timestamp'. If not
    # just return "".
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        val = self.store.get(key, [])
        l = 0
        r = len(val)
        while l <= r:
            m = (l + r) // 2
            # if we find that our obtained val is less than timestamp
            # we adjust our range to the left and see if there is a bigger timestamp
            # closer to the timestamp that was input into the function
            if val[m][1] <= timestamp:
                res = val[m][0]
                l = m + 1
            else:
                l = m - 1
        return res