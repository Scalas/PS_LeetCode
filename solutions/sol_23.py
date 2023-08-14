from typing import List, Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def merge_k_lists(lists: List[Optional[ListNode]]):
        if not lists:
            return None

        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            res = ListNode(0)
            pos = res
            while l1 and l2:
                if l1.val < l2.val:
                    pos.next = l1
                    l1 = l1.next
                    pos = pos.next
                    continue
                if l1.val >= l2.val:
                    pos.next = l2
                    l2 = l2.next
                    pos = pos.next
            while l1:
                pos.next = l1
                l1 = l1.next
                pos = pos.next
            while l2:
                pos.next = l2
                l2 = l2.next
                pos = pos.next
            return res.next

        while len(lists) > 1:
            nlists = []
            while len(lists) > 1:
                nlists.append(merge(lists.pop(), lists.pop()))
            if lists:
                nlists.append(lists.pop())
            lists = nlists
        return lists[0]
