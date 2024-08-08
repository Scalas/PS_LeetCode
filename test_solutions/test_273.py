import pytest
from solutions.sol_273 import Solution


cases = [
    {
        "input": {"num": 123},
        "output": "One Hundred Twenty Three",
    },
    {
        "input": {"num": 12345},
        "output": "Twelve Thousand Three Hundred Forty Five",
    },
    {
        "input": {"num": 1234567},
        "output": "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
    },
]


@pytest.mark.sol273
def test_run():
    for case in cases:
        assert (
            Solution.number_to_words(
                num=case["input"]["num"],
            )
            == case["output"]
        )
