import pytest
from solutions.sol_1339 import Solution
from converter.leet_code_converter import list_to_tree

cases = [
    {
        'input': {
            'tree': [1, 2, 3, 4, 5, 6]
        },
        'output': 110
    },
    {
        'input': {
            'tree': [1, None, 2, None, None, 3, 4, None, None, None, None, None, None, 5, 6]
        },
        'output': 90
    },
]


@pytest.mark.sol1339
def test_run():
    for case in cases:
        assert Solution.max_product(
            root=list_to_tree(case['input']['tree'])
        ) == case['output']
