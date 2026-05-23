def possible(d, arr, k):
    count = 0
    for i in range(len(arr) - 1):
        count += int((arr[i + 1] - arr[i]) / d)
    return count <= k 

class solution:
    def minMaxDistance(self, arr, k):
        low = 0
        high = 1e8
        while high - low > 1e-6:
            mid = (low + high) / 2.0
            if possible(mid, arr, k):
                high = mid 
            else:
                low = mid 
        return low 