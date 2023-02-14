import pytest
from solutions.sol_67 import Solution

cases = [
    {
        'input': {
            'a': '11',
            'b': '1'
        },
        'output': '100'
    },
    {
        'input': {
            'a': '1010',
            'b': '1011'
        },
        'output': '10101'
    },
]


@pytest.mark.sol67
def test_run():
    for case in cases:
        assert Solution.add_binary(
            a=case['input']['a'],
            b=case['input']['b']
        ) == case['output']
