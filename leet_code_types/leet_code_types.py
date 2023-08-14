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
        self.next = None
