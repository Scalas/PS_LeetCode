from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def average_of_subtree(root: Optional[TreeNode]) -> int:
        answer = 0

        def count(cur):
            nonlocal answer
            s = cur.val
            cnt = 1
            if cur.left:
                res = count(cur.left)
                s += res[0]
                cnt += res[1]
            if cur.right:
                res = count(cur.right)
                s += res[0]
                cnt += res[1]
            if cur.val == s // cnt:
                answer += 1
            return s, cnt

        count(root)
        return answer
