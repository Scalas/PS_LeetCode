import pytest
from solutions.sol_1980 import Solution

cases = [
    {
        "input": {
            "nums": ["01", "10"],
        },
        "output": {"00", "11"},
    },
    {
        "input": {
            "nums": ["00", "01"],
        },
        "output": {"10", "11"},
    },
    {
        "input": {
            "nums": ["111", "011", "001"],
        },
        "output": {"000", "010", "100", "101", "110"},
    },
]


@pytest.mark.sol_1980
def test_run():
    for case in cases:
        assert (
            Solution.find_different_binary_string(
                nums=case["input"]["nums"],
            )
            in case["output"]
        )
