from typing import List


class Solution:
    @staticmethod
    def leftmost_building_queries(
        heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(heights)
        queries = list(map(sorted, queries))
        queries = sorted(
            [queries[i] + [i] for i in range(len(queries))], key=lambda x: -x[1]
        )

        def reverse_bisect(arr, num):
            s, e = 0, len(arr) - 1
            res = -1
            while s <= e:
                mid = (s + e) // 2
                if arr[mid][0] > num:
                    res = arr[mid][1]
                    s = mid + 1
                else:
                    e = mid - 1
            return res

        answer = [-1] * len(queries)
        st = []
        idx = n - 1
        for u, v, qi in queries:
            if u > v:
                u, v = v, u
            if u == v or heights[v] > heights[u]:
                answer[qi] = v
                continue
            while idx > v:
                h = heights[idx]
                while st and h > st[-1][0]:
                    st.pop()
                st.append([h, idx])
                idx -= 1
            answer[qi] = reverse_bisect(st, heights[u])
        return answer
