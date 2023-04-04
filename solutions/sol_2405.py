class Solution:
    @staticmethod
    def partition_string(s: str) -> int:
        answer = 0
        count = set()
        for c in s:
            if c in count:
                answer += 1
                count = {c}
            else:
                count.add(c)
        if count:
            answer += 1
        return answer
