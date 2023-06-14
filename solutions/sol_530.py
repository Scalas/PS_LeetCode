from typing import Optional

from leet_code_types.leet_code_types import TreeNode

INF = 10 ** 9


class Solution:
    @staticmethod
    def get_minimum_difference(root: Optional[TreeNode]) -> int:
        def in_order(cur, pre_val):
            min_diff = INF
            if cur.left:
                pre_val, left_min_diff = in_order(cur.left, pre_val)
                min_diff = min(min_diff, left_min_diff)
            if pre_val != -1:
                min_diff = min(min_diff, cur.val - pre_val)
            if cur.right:
                pre_val, right_min_diff = in_order(cur.right, cur.val)
                min_diff = min(min_diff, right_min_diff)
            return max(cur.val, pre_val), min_diff

        return in_order(root, -1)[1]
