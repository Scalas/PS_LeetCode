class Solution:
    @staticmethod
    def min_deletions(s: str) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        count = [i for i in count if i]
        count.sort(reverse=True)
        print(count)
        answer = 0
        pre = 10**9
        for i in range(len(count)):
            c = count[i]
            if c >= pre:
                if pre:
                    answer += c - pre + 1
                    count[i] = pre - 1
                else:
                    answer += c
                    count[i] = 0
            pre = count[i]
        return answer
