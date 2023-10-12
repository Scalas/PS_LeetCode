from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class QuadTreeNode:
    def __init__(
        self,
        val,
        is_leaf,
        top_left=None,
        top_right=None,
        bottom_left=None,
        bottom_right=None,
    ):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class ListNodeWithRandomPointer:
    def __init__(self, x=0, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


class MountainArray:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)
