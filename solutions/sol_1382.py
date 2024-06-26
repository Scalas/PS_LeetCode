from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def balance_bst(root: TreeNode) -> TreeNode:
        nodes = []

        def dfs(cur):
            if cur.left:
                dfs(cur.left)
            nodes.append(cur)
            if cur.right:
                dfs(cur.right)

        def build(s, e):
            if s > e:
                return None
            if s == e:
                nodes[s].left = None
                nodes[s].right = None
                return nodes[s]
            mid = (s + e) // 2
            cur = nodes[mid]
            cur.left = build(s, mid - 1)
            cur.right = build(mid + 1, e)
            return cur

        dfs(root)
        return build(0, len(nodes) - 1)
