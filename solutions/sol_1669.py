from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def merge_in_between(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cursor = list1
        start, end = None, None
        for i in range(b + 1):
            if i == a - 1:
                start = cursor
            cursor = cursor.next
        end = cursor

        answer = list1
        if start:
            start.next = list2
        else:
            answer = list2

        cursor = list2
        while cursor.next:
            cursor = cursor.next
        cursor.next = end

        return answer
