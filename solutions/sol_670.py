class Solution:
    @staticmethod
    def maximum_swap(num: int) -> int:
        answer = num
        num = list(str(num))
        n = len(num)

        for i in range(n):
            for j in range(i + 1, n):
                cnum = num[:]
                cnum[i], cnum[j] = cnum[j], cnum[i]
                answer = max(answer, int("".join(cnum)))
        return answer
