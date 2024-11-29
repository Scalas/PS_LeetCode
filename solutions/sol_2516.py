from typing import List


class Solution:
    @staticmethod
    def take_characters(s: str, k: int) -> int:
        n = len(s)
        characters: List[int] = list(map(lambda x: ord(x) - ord("a"), list(s)))
        total_count = [0] * 3
        for character in characters:
            total_count[character] += 1
        if min(total_count) < k:
            return -1

        def check(window):
            nonlocal n, k, s
            count = [0] * 3
            for c in characters[n - window :]:
                count[c] += 1
            if min(count) >= k:
                return True

            left = n - window
            for c in characters[:window]:
                count[c] += 1
                count[characters[left]] -= 1
                left += 1
                if min(count) >= k:
                    return True
            return False

        s, e = 0, n
        answer = n
        while s <= e:
            mid = (s + e) // 2
            if check(mid):
                answer = min(answer, mid)
                e = mid - 1
            else:
                s = mid + 1
        return answer
