from typing import List, Optional
from leet_code_types.leet_code_types import TreeNode


def list_to_tree(tree: List[int]) -> Optional[TreeNode]:

    if not tree:
        return

    n = len(tree)
    root = TreeNode()
    root.val = tree[0]
    q = [root]
    idx = 1

    q = [root]
    while q and idx < n:
        nq = []
        for cur in q:
            left = tree[idx]
            if left is not None:
                cur.left = TreeNode()
                cur.left.val = left
                nq.append(cur.left)
            idx += 1

            if idx == n:
                break

            right = tree[idx]
            if right is not None:
                cur.right = TreeNode()
                cur.right.val = right
                nq.append(cur.right)
            idx += 1
        q = nq
    return root
