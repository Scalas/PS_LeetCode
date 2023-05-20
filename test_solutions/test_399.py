import pytest
from solutions.sol_399 import Solution

cases = [
    {
        'input': {
            'equations': [["a", "b"], ["b", "c"]],
            'values': [2.0, 3.0],
            'queries': [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        },
        'output': [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    },
    {
        'input': {
            'equations': [["a", "b"], ["b", "c"], ["bc", "cd"]],
            'values': [1.5, 2.5, 5.0],
            'queries': [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        },
        'output': [3.75000, 0.40000, 5.00000, 0.20000]
    },
    {
        'input': {
            'equations': [["a", "b"]],
            'values': [0.5],
            'queries': [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        },
        'output': [0.50000, 2.00000, -1.00000, -1.00000]
    },
]


@pytest.mark.sol_399
def test_run():
    for case in cases:
        assert Solution.calc_equation(
            equations=case['input']['equations'],
            values=case['input']['values'],
            queries=case['input']['queries'],
        ) == case['output']
