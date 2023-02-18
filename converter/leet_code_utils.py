from typing import List, Optional
from leet_code_types.leet_code_types import TreeNode


def list_to_tree(tree: List[int]) -> Optional[TreeNode]:

    if not tree:
        return

    n = len(tree)
    root = TreeNode()
    root.val = tree[0]
    idx = 1

    q = [root]
    while q and idx < n:
        nq = []
        for cur in q:
            if idx == n:
                break

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


def compare_tree(t1: Optional[TreeNode], t2: Optional[TreeNode]):
    def compare(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        try:
            if node1.val != node2.val:
                return False
            if node1.left:
                if not compare(node1.left, node2.left):
                    return False
            if node1.right:
                if not compare(node1.right, node2.right):
                    return False
            return True
        except:
            return False

    try:
        if t1:
            if compare(t1, t2):
                return True
        else:
            if not t2:
                return True
        return False
    except:
        return False
