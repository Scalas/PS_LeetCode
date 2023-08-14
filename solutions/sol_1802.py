class Solution:
    @staticmethod
    def max_value(n: int, index: int, max_sum: int) -> int:
        def check(num):
            res = num * (num + 1) - num
            ldiff = num - index - 1
            rdiff = num - n + index
            if ldiff > 0:
                res -= ldiff * (ldiff + 1) // 2
            else:
                res -= ldiff
            if rdiff > 0:
                res -= rdiff * (rdiff + 1) // 2
            else:
                res -= rdiff
            return res <= max_sum

        s, e = 1, max_sum
        answer = 1
        while s <= e:
            mid = (s + e) // 2
            if check(mid):
                answer = mid
                s = mid + 1
            else:
                e = mid - 1
        return answer
