import pytest
from solutions.sol_2264 import Solution

cases = [
    {"input": {"num": "6777133339"}, "output": "777"},
    {"input": {"num": "2300019"}, "output": "000"},
    {"input": {"num": "42352338"}, "output": ""},
]


@pytest.mark.sol_2264
def test_run():
    for case in cases:
        assert Solution.largest_good_integer(num=case["input"]["num"]) == case["output"]
