from typing import List, Optional
from leet_code_types.leet_code_types import TreeNode


def list_to_tree(tree: List[int]) -> Optional[TreeNode]:

    if not tree:
        return

    n = len(tree)
    root = TreeNode()

    def dfs(cur: int, cur_node: TreeNode):
        cur_node.val = tree[cur]
        left = cur * 2 + 1
        if left < n and tree[left]:
            cur_node.left = TreeNode()
            dfs(left, cur_node.left)
        right = cur * 2 + 2
        if right < n and tree[right]:
            cur_node.right = TreeNode()
            dfs(right, cur_node.right)

    dfs(0, root)
    return root
