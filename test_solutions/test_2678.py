import pytest
from solutions.sol_2678 import Solution


cases = [
    {
        "input": {"details": ["7868190130M7522", "5303914400F9211", "9273338290F4010"]},
        "output": 2,
    },
    {
        "input": {"details": ["1313579440F2036", "2921522980M5644"]},
        "output": 0,
    },
]


@pytest.mark.sol2678
def test_run():
    for case in cases:
        assert (
            Solution.count_seniors(
                details=case["input"]["details"],
            )
            == case["output"]
        )
