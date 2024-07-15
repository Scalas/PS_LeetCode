import pytest
from solutions.sol_726 import Solution


cases = [
    {
        "input": {"formula": "H2O"},
        "output": "H2O",
    },
    {
        "input": {"formula": "Mg(OH)2"},
        "output": "H2MgO2",
    },
    {
        "input": {"formula": "K4(ON(SO3)2)2"},
        "output": "K4N2O14S4",
    },
]


@pytest.mark.sol726
def test_run():
    for case in cases:
        assert (
            Solution.count_of_atoms(
                formula=case["input"]["formula"],
            )
            == case["output"]
        )
