from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def remove_zero_sum_sub_lists(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        st = []
        val_st = []
        while head:
            st.append(head)
            acc = head.val
            if val_st:
                acc += val_st[-1]
            val_st.append(acc)
            if acc == 0:
                st = []
                val_st = []
            else:
                for i in range(len(val_st) - 1):
                    if acc - val_st[i] == 0:
                        st = st[: i + 1]
                        val_st = val_st[: i + 1]
                        break
            head = head.next
        for i in range(len(st) - 1):
            st[i].next = st[i + 1]
        if st:
            st[-1].next = None
        return None if not st else st[0]
