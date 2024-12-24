from typing import List


class Solution:
    @staticmethod
    def minimum_diameter_after_merge(
        edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        n, m = len(edges1) + 1, len(edges2) + 1
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(m)]
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)

        def dfs(g, md, sd, vs, cur):
            vs[cur] = True
            res = -1
            second = -1
            for nxt in g[cur]:
                if vs[nxt]:
                    continue
                d = dfs(g, md, sd, vs, nxt)
                if d >= res:
                    second = res
                    res = d
            md[cur] = res + 1
            sd[cur] = second + 1
            return res + 1

        def dfs2(g, md, sd, vs, cur, p):
            vs[cur] = True
            if p >= md[cur]:
                sd[cur] = md[cur]
                md[cur] = p
            children = [child for child in g[cur] if not vs[child]]
            if not children:
                return
            if len(children) == 1:
                dfs2(g, md, sd, vs, children[0], p + 1)
            else:
                children.sort(key=lambda x: md[x])
                fm, sm = md[children[-1]] + 2, md[children[-2]] + 2
                for child in children[: len(children) - 1]:
                    dfs2(g, md, sd, vs, child, max(p + 1, fm))
                dfs2(g, md, sd, vs, children[-1], max(p + 1, sm))

        def get_im_md(graph, count):
            max_depth = [-1] * count
            second_depth = [-1] * count
            visited = [False] * count
            dfs(graph, max_depth, second_depth, visited, 0)
            visited = [False] * count
            dfs2(graph, max_depth, second_depth, visited, 0, 0)
            im = 0
            for i in range(count):
                im = max(im, max_depth[i] + second_depth[i])
            md = min(max_depth)
            return [im, md]

        g1_im, g1_md = get_im_md(g1, n)
        g2_im, g2_md = get_im_md(g2, m)

        return max(g1_im, g2_im, g1_md + g2_md + 1)
