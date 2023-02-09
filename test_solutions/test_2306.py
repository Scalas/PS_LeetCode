import pytest
from solutions.sol_2306 import Solution

cases = [
    {
        'input': {
            'ideas': ["coffee","donuts","time","toffee"],
        },
        'output': 6
    },
    {
        'input': {
            'ideas': ["lack","back"],
        },
        'output': 0
    },
]


@pytest.mark.sol_2306
def test_run():
    for case in cases:
        assert Solution.distinct_names(
            ideas=case['input']['ideas'],
        ) == case['output']
