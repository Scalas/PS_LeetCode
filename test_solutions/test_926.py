import pytest
from solutions.sol_926 import Solution

cases = [
    {
        'input': {
            's': '00110',
        },
        'output': 1
    },
    {
        'input': {
            's': '010110',
        },
        'output': 2
    },
    {
        'input': {
            's': '00011000',
        },
        'output': 2
    },
]


@pytest.mark.sol926
def test_run():
    for case in cases:
        assert Solution.min_flips_mono_increasing(
            s=case['input']['s']
        ) == case['output']
