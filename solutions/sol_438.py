from typing import List


class Solution:
    @staticmethod
    def find_anagrams(s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []
        s_count = [0] * 26
        p_count = [0] * 26
        a_ord = ord("a")
        for i in range(m):
            s_count[ord(s[i]) - a_ord] += 1
            p_count[ord(p[i]) - a_ord] += 1

        answer = []
        if s_count == p_count:
            answer.append(0)
        for i in range(n - m):
            s_count[ord(s[m + i]) - a_ord] += 1
            s_count[ord(s[i]) - a_ord] -= 1
            if s_count == p_count:
                answer.append(i + 1)
        return answer
