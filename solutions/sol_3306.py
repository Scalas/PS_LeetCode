class Solution:
    @staticmethod
    def count_of_substrings(word: str, k: int) -> int:
        n = len(word)
        vr = [0] * n
        count = [0] * 6

        def index(char):
            if char == "a":
                return 0
            if char == "e":
                return 1
            if char == "i":
                return 2
            if char == "o":
                return 3
            if char == "u":
                return 4
            return 5

        vc = 0
        for i in range(n - 1, -1, -1):
            vr[i] = vc
            if index(word[i]) < 5:
                vc += 1
            else:
                vc = 0
        print(vr)

        answer = 0
        start = 0
        for i in range(n):
            c = word[i]
            count[index(c)] += 1
            while count[5] > k:
                count[index(word[start])] -= 1
                start += 1
            if min(count[:5]) == 0:
                continue
            r = vr[i]
            while min(count[:5]) > 0 and count[5] == k:
                answer += r + 1
                count[index(word[start])] -= 1
                start += 1
        return answer
