from typing import Optional

from leet_code_types.leet_code_types import TreeNode, ListNode


class Solution:
    @staticmethod
    def is_sub_path(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        sub = []
        while head:
            sub.append(head.val)
            head = head.next
        n = len(sub)

        def dfs(cur, path):
            path.append(cur.val)
            last = path[-n:]
            if last == sub:
                return True
            if cur.left:
                if dfs(cur.left, path):
                    return True
            if cur.right:
                if dfs(cur.right, path):
                    return True
            path.pop()

        if dfs(root, []):
            return True

        return False
