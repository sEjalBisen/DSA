class solution:
    def hasHalf(self, arr, n):
        s = set()
        for num in arr:
            if((num % 2 == 0 and (num // 2) in s)) or (2 * num in s):
                return True
            s.add(num)
        return False