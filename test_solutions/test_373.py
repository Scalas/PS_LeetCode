import pytest
from solutions.sol_373 import Solution

cases = [
    {
        'input': {
            'nums1': [1, 7, 11],
            'nums2': [2, 4, 6],
            'k': 3,
        },
        'output': [[1, 2], [1, 4], [1, 6]],
    },
    {
        'input': {
            'nums1': [1, 1, 2],
            'nums2': [1, 2, 3],
            'k': 2,
        },
        'output': [[1, 1], [1, 1]],
    },
    {
        'input': {
            'nums1': [1, 2],
            'nums2': [3],
            'k': 3,
        },
        'output': [[1, 3], [2, 3]],
    },
]


@pytest.mark.sol373
def test_run():
    for case in cases:
        assert Solution.k_smallest_pairs(
            nums1=case['input']['nums1'],
            nums2=case['input']['nums2'],
            k=case['input']['k'],
        ) == case['output']
