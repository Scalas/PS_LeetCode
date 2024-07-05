from typing import Optional, List

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def nodes_between_critical_points(head: Optional[ListNode]) -> List[int]:
        idx = 1
        cur = head.next
        pre_val = head.val
        critical = []
        while cur.next:
            val = cur.val
            next_val = cur.next.val
            if val > pre_val and val > next_val or val < pre_val and val < next_val:
                critical.append(idx)
            cur = cur.next
            pre_val = val
            idx += 1
        if len(critical) < 2:
            return [-1, -1]
        return [
            min([critical[i + 1] - critical[i] for i in range(len(critical) - 1)]),
            critical[-1] - critical[0],
        ]
