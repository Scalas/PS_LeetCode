from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def delete_node(node: ListNode):
        node.val = node.next.val
        node.next = node.next.next
