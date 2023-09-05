from typing import List, Optional
from leet_code_types.leet_code_types import TreeNode, QuadTreeNode, ListNode, ListNodeWithRandomPointer


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


def tree_to_list(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    q = [root]
    while q:
        nq = []
        for cur in q:
            if not cur:
                res.append(None)
            else:
                res.append(cur.val)
                nq.append(cur.left)
                nq.append(cur.right)
        q = nq
    while res and res[-1] is None:
        res.pop()
    return res


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


def list_to_linked_list(python_list: List[int]) -> Optional[ListNode]:
    if not python_list:
        return None

    head = ListNode(python_list[0])
    pos = head
    for num in python_list[1:]:
        pos.next = ListNode(num)
        pos = pos.next

    return head


def list_to_cyclic_linked_list(
        python_list: List[int], cycle_start
) -> List[Optional[ListNode]]:
    if not python_list:
        return [None, None]

    head = ListNode(python_list[0])
    pos = head
    cycle_start_node = None
    for i in range(len(python_list)):
        num = python_list[i]
        pos.next = ListNode(num)
        pos = pos.next
        if i == cycle_start:
            cycle_start_node = pos
    pos.next = cycle_start_node
    return [head, cycle_start_node]


def list_to_linked_list_with_random_pointer(python_list: List[List[int]]) -> Optional[ListNodeWithRandomPointer]:
    if not python_list:
        return None

    res = []
    for i in range(len(python_list)):
        value, random = python_list[i]
        node = ListNodeWithRandomPointer(value)
        res.append([node, i + 1, random])
    for node, next, random in res:
        node.next = None if next == len(res) else res[next][0]
        node.random = None if not random else res[random][0]

    return res[0][0] if res else None


def compare_linked_list(list_1: Optional[ListNode], list_2: Optional[ListNode]) -> bool:
    while list_1 and list_2:
        if list_1.val != list_2.val:
            return False
        list_1 = list_1.next
        list_2 = list_2.next
    if list_1 or list_2:
        return False
    return True


def compare_linked_list_with_random_pointer(
        list_1: Optional[ListNodeWithRandomPointer],
        list_2: Optional[ListNodeWithRandomPointer]
) -> bool:
    while list_1 and list_2:
        if list_1 == list_2:
            return False
        if list_1.val != list_2.val:
            return False
        if list_1.random is None or list_2.random is None:
            if list_1.random != list_2.random:
                return False
        if list_1.random is not None and list_2.random is not None:
            if list_1.random.val != list_2.random.val:
                return False

        list_1 = list_1.next
        list_2 = list_2.next
    if list_1 or list_2:
        return False
    return True


def find_from_tree(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    q = [root]
    while q:
        nq = []
        for cur in q:
            if cur.val == target:
                return cur
            if cur.left:
                nq.append(cur.left)
            if cur.right:
                nq.append(cur.right)
        q = nq
