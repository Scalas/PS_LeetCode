from typing import Optional

from leet_code_types.leet_code_types import ListNode, TreeNode


class Solution:
    @staticmethod
    def sorted_list_to_bst(head: Optional[ListNode]) -> Optional[TreeNode]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        n = len(nodes)

        if not nodes:
            return None

        def build_tree(node_list, s, e):
            if s > e:
                return None
            mid = (s + e) // 2
            root = TreeNode(node_list[mid])
            if s == e:
                return root
            root.left = build_tree(node_list, s, mid - 1)
            root.right = build_tree(node_list, mid + 1, e)
            return root

        return build_tree(nodes, 0, n - 1)
