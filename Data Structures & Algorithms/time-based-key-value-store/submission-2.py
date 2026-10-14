class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.storage:
            self.storage[key].append([value, timestamp])
        else:
            self.storage[key] = [[value, timestamp]]

        # print(self.storage[key])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.storage:
            logs = self.storage[key]
        else:
            return ""

        if logs[0][1] > timestamp:
            return ""

        left, right = 0, len(logs) - 1

        # standard binary search, if timestamp greater/less than then set it as right/left. Eventually you get to a state where mid = left, then you return that as the timestamp value


        # 0 1 2 3 4 5

        while left <= right:
            mid = (left + right) // 2

            if logs[mid][1] > timestamp:
                right = mid - 1
            elif logs[mid][1] < timestamp:
                left = mid + 1
            else:
                return logs[mid][0]
            
        return logs[right][0]



