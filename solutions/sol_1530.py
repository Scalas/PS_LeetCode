from collections import defaultdict
from typing import Dict, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def count_pairs(root: TreeNode, distance: int) -> int:
        leaf_nodes = set()
        g: Dict[int, List[int]] = defaultdict(list)
        idx = 0

        def dfs(cur: TreeNode):
            nonlocal leaf_nodes, idx
            idx += 1
            cur_id = idx
            is_leaf = True
            if cur.left:
                nxt_id = dfs(cur.left)
                g[cur_id].append(nxt_id)
                g[nxt_id].append(cur_id)
                is_leaf = False
            if cur.right:
                nxt_id = dfs(cur.right)
                g[cur_id].append(nxt_id)
                g[nxt_id].append(cur_id)
                is_leaf = False
            if is_leaf:
                leaf_nodes.add(cur_id)
            return cur_id

        dfs(root)
        answer = 0
        for node in leaf_nodes:
            q = [node]
            visited: Dict[int, bool] = defaultdict(bool)
            visited[node] = True
            for _ in range(distance):
                if not q:
                    break
                nq = []
                for cur in q:
                    for nxt in g[cur]:
                        if visited[nxt]:
                            continue
                        visited[nxt] = True
                        nq.append(nxt)
                        if nxt in leaf_nodes:
                            answer += 1
                q = nq
        return answer // 2
