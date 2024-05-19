from typing import List


class Solution:
    @staticmethod
    def maximumValueSum(nums: List[int], k: int, edges: List[List[int]]) -> int:
        rev_nums = list(map(lambda x: (x & ~k) | (~x & k), nums))
        n = len(nums)
        g: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(cur):
            visited[cur] = True
            base = 0
            rev_cand = []
            is_leaf = True
            min_loss = 0
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                is_leaf = False
                num, rev_num = nums[nxt], rev_nums[nxt]
                if rev_num < num:
                    min_loss = max(min_loss, rev_num - num)
                org, rev = dfs(nxt)

                # can be achieved with no reverse
                org_max = max(org, rev)

                # can be achieved with reverse
                org_rev, rev_rev = org - num + rev_num, rev - rev_num + num
                rev_max = max(org_rev, rev_rev) if rev != -1 else org_rev

                base += org_max
                rev_cand.append(rev_max - org_max)
            if is_leaf:
                return nums[cur], -1
            cnt = len(rev_cand)
            rev_cand.sort(reverse=True)
            cur_org_max = base + nums[cur]
            for i in range(0, cnt - 1, 2):
                diff = rev_cand[i] + rev_cand[i + 1]
                if diff > 0:
                    cur_org_max += diff
                else:
                    break
            cur_rev_max = base + rev_nums[cur] + rev_cand[0]
            for i in range(1, cnt - 1, 2):
                diff = rev_cand[i] + rev_cand[i + 1]
                if diff > 0:
                    cur_rev_max += diff
                else:
                    break
            return cur_org_max, cur_rev_max

        visited = [False] * n
        return max(dfs(0))
