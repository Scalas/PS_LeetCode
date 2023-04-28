import pytest
from solutions.sol_797 import Solution


cases = [
    {
        'input': {
            'graph': [[1, 2], [3], [3], []],
        },
        'output': [[0, 1, 3], [0, 2, 3]],
    },
    {
        'input': {
            'graph': [[4, 3, 1], [3, 2, 4], [3], [4], []],
        },
        'output': [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
    },
]


@pytest.mark.sol_797
def test_run():
    for case in cases:
        assert Solution.all_paths_source_target(
            graph=case['input']['graph']
        ) == case['output']
