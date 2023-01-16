import pytest
from solutions.sol_57 import Solution

cases = [
    {
        'input': {
            'intervals': [[1,3],[6,9]],
            'new_interval': [2,5]
        },
        'output': [[1,5],[6,9]]
    },
    {
        'input': {
            'intervals': [[1,2],[3,5],[6,7],[8,10],[12,16]],
            'new_interval': [4,8]
        },
        'output': [[1,2],[3,10],[12,16]]
    },
    {
        'input': {
            'intervals': [[0,1],[5,5],[6,7],[9,11]],
            'new_interval': [12,21]
        },
        'output': [[0,1],[5,5],[6,7], [9, 11], [12, 21]]
    },
]


@pytest.mark.sol57
def test_run():
    for case in cases:
        assert Solution.insert(
            intervals=case['input']['intervals'],
            new_interval=case['input']['new_interval']
        ) == case['output']
