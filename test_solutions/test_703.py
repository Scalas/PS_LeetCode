import pytest
from solutions.sol_703 import KthLargest
from converter.leet_code_utils import list_to_tree

cases = [
    {
        "input": {
            "command": ["KthLargest", "add", "add", "add", "add", "add"],
            "args": [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
        },
        "output": [None, 4, 5, 5, 8, 8],
    },
]


@pytest.mark.sol_703
def test_run():
    for case in cases:
        args = case["input"]["args"]
        kth = KthLargest(args[0][0], args[0][1])
        result = [None]
        for arg in args[1:]:
            result.append(kth.add(arg[0]))
        assert result == case["output"]
