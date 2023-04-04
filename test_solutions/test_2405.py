import pytest
from solutions.sol_2405 import Solution

cases = [
    {
        'input': {
            's': 'abacaba',
        },
        'output': 4,
    },
    {
        'input': {
            's': 'ssssss',
        },
        'output': 6,
    },
]


@pytest.mark.sol_2405
def test_run():
    for case in cases:
        assert Solution.partition_string(
            s=case['input']['s'],
        ) == case['output']
