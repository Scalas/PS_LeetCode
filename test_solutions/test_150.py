import pytest
from solutions.sol_150 import Solution

cases = [
    {
        'input': {
            'tokens': ["2","1","+","3","*"]
        },
        'output': 9
    },
    {
        'input': {
            'tokens': ["4","13","5","/","+"]
        },
        'output': 6
    },
    {
        'input': {
            'tokens': ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        },
        'output': 22
    },
]


@pytest.mark.sol150
def test_run():
    for case in cases:
        assert Solution.eval_rpn(
            tokens=case['input']['tokens']
        ) == case['output']
