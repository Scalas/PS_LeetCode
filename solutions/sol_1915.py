class Solution:
    @staticmethod
    def wonderful_substrings(word: str) -> int:
        def xor(a, b):
            return (a & ~b) | (~a & b)

        word = list(map(lambda x: ord(x) - ord("a"), word))
        n = len(word)
        state = [0] * n
        cur = 0
        for i in range(n):
            c = word[i]
            key = 1 << c
            cur = xor(cur, key)
            state[i] = cur

        count = [0] * (1 << 10)
        count[0] += 1
        for s in state:
            count[s] += 1

        answer = 0
        for s in state:
            count[s] -= 1
            answer += count[s]
            for i in range(10):
                answer += count[xor(s, 1 << i)]
        return answer
