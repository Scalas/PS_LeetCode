import pytest
from solutions.sol_1455 import Solution


cases = [
    {
        "input": {"sentence": "i love eating burger", "searchWord": "burg"},
        "output": 4,
    },
    {
        "input": {"sentence": "this problem is an easy problem", "searchWord": "pro"},
        "output": 2,
    },
    {
        "input": {"sentence": "i am tired", "searchWord": "you"},
        "output": -1,
    },
]


@pytest.mark.sol1455
def test_run():
    for case in cases:
        assert (
            Solution.is_prefix_of_word(
                searchWord=case["input"]["searchWord"],
                sentence=case["input"]["sentence"],
            )
            == case["output"]
        )
