from typing import List


class Solution:
    @staticmethod
    def restore_ip_addresses(s: str) -> List[str]:
        n = len(s)
        answer = []
        address = [[] for _ in range(4)]

        def dfs(cur, slot):
            if cur == n:
                if slot == 4:
                    answer.append('.'.join(map(lambda x: ''.join(x), address)))
                return

            if slot < 4:
                address[slot].append(s[cur])
                dfs(cur + 1, slot + 1)
                address[slot].pop()
            if slot > 0:
                if address[slot - 1][0] == '0':
                    return
                address[slot - 1].append(s[cur])
                if int(''.join(address[slot - 1])) > 255:
                    address[slot - 1].pop()
                    return
                dfs(cur + 1, slot)
                address[slot - 1].pop()
        dfs(0, 0)
        return answer
