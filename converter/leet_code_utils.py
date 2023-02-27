from typing import List, Optional
from leet_code_types.leet_code_types import TreeNode, QuadTreeNode


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


def list_to_quad_tree(tree: List[List[int]]) -> Optional[QuadTreeNode]:

    if not tree:
        return

    n = len(tree)
    root = QuadTreeNode(val=tree[0][1], is_leaf=tree[0][0])
    idx = 1

    q = [root]
    while q and idx < n:
        nq = []
        for cur in q:
            if idx == n:
                break

            top_left = tree[idx]
            if top_left is not None:
                cur.top_left = QuadTreeNode(val=tree[idx][1], is_leaf=tree[idx][0])
                nq.append(cur.top_left)
            idx += 1
            if idx == n:
                break

            top_right = tree[idx]
            if top_right is not None:
                cur.top_right = QuadTreeNode(val=tree[idx][1], is_leaf=tree[idx][0])
                nq.append(cur.top_right)
            idx += 1
            if idx == n:
                break

            bottom_left = tree[idx]
            if bottom_left is not None:
                cur.bottom_left = QuadTreeNode(val=tree[idx][1], is_leaf=tree[idx][0])
                nq.append(cur.bottom_left)
            idx += 1
            if idx == n:
                break

            bottom_right = tree[idx]
            if bottom_right is not None:
                cur.bottom_right = QuadTreeNode(val=tree[idx][1], is_leaf=tree[idx][0])
                nq.append(cur.bottom_right)
            idx += 1
        q = nq
    return root


def compare_quad_tree(t1: Optional[QuadTreeNode], t2: Optional[QuadTreeNode]):
    def compare(node1: Optional[QuadTreeNode], node2: Optional[QuadTreeNode]) -> bool:
        try:
            if node1.val != node2.val:
                return False
            if node1.is_leaf != node2.is_leaf:
                return False
            if node1.top_left:
                if not compare(node1.top_left, node2.top_left):
                    return False
            if node1.top_right:
                if not compare(node1.top_right, node2.top_right):
                    return False
            if node1.bottom_left:
                if not compare(node1.bottom_left, node2.bottom_left):
                    return False
            if node1.bottom_right:
                if not compare(node1.bottom_right, node2.bottom_right):
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
