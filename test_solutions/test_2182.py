import pytest
from solutions.sol_2182 import Solution


cases = [
    {
        "input": {"s": "cczazcc", "repeat_limit": 3},
        "output": "zzcccac",
    },
    {
        "input": {"s": "aababab", "repeat_limit": 2},
        "output": "bbabaa",
    },
    {
        "input": {"s": "robnsdvpuxbapuqgopqvxdrchivlifeepy", "repeat_limit": 2},
        "output": "yxxvvuvusrrqqppopponliihgfeeddcbba",
    },
]


@pytest.mark.sol2182
def test_run():
    for case in cases:
        assert (
            Solution.repeat_limited_string(
                s=case["input"]["s"],
                repeat_limit=case["input"]["repeat_limit"],
            )
            == case["output"]
        )
