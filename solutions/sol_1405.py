class Solution:
    @staticmethod
    def longest_diverse_string(a: int, b: int, c: int) -> str:
        res = []
        banned = -1
        count = [a, b, c]
        while True:
            target = max([i for i in range(3) if i != banned], key=lambda x: count[x])
            cnt = count[target]
            if cnt == 0:
                break
            v = min(cnt, 2)
            count[target] -= v
            res.extend([target] * v)
            banned = target
        for i in range(3):
            end = False
            while not end and count[i] > 0:
                end = True
                for j in range(len(res) - 1):
                    if j > 0 and res[j - 1] == res[j] == i:
                        continue
                    if j > 1 and res[j - 2] == res[j - 1] == i:
                        continue
                    if res[j] == res[j + 1] == i:
                        continue
                    res.insert(j, i)
                    count[i] -= 1
                    end = False
                    break

        return "".join(map(lambda x: chr(x + ord("a")), res))
