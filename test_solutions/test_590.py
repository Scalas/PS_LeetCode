import pytest

from leet_code_types.leet_code_types import NaryTreeNode
from solutions.sol_590 import Solution


cases = [
    {
        "input": {
            "root": NaryTreeNode(
                1,
                [
                    NaryTreeNode(
                        3,
                        [
                            NaryTreeNode(5, []),
                            NaryTreeNode(6, []),
                        ],
                    ),
                    NaryTreeNode(2, []),
                    NaryTreeNode(4, []),
                ],
            ),
        },
        "output": [5, 6, 3, 2, 4, 1],
    },
    {
        "input": {
            "root": NaryTreeNode(
                1,
                [
                    NaryTreeNode(2, []),
                    NaryTreeNode(
                        3,
                        [
                            NaryTreeNode(6, []),
                            NaryTreeNode(
                                7,
                                [
                                    NaryTreeNode(
                                        11,
                                        [
                                            NaryTreeNode(14, []),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    NaryTreeNode(
                        4,
                        [
                            NaryTreeNode(
                                8,
                                [
                                    NaryTreeNode(12, []),
                                ],
                            ),
                        ],
                    ),
                    NaryTreeNode(
                        5,
                        [
                            NaryTreeNode(
                                9,
                                [
                                    NaryTreeNode(13, []),
                                ],
                            ),
                            NaryTreeNode(10, []),
                        ],
                    ),
                ],
            ),
        },
        "output": [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
    },
]


@pytest.mark.sol590
def test_run():
    for case in cases:
        assert (
            Solution.postorder(
                root=case["input"]["root"],
            )
            == case["output"]
        )
