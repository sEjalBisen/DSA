MOD = 1000000007
def power(x, n):
    if n == 0:
        return 1 
    half = power(x, n // 2)
    result = (half * half) % MOD 
    if n % 2 != 0:
        result = (result * x) % MOD 
    return result


class solution:
    def countGoodStrings(self, n):
        oddPlaces = n // 2 
        evenPlaces = n // 2 + n % 2 
        return (power(5, evenPlaces) * power(4, oddPlaces)) % MOD 
        