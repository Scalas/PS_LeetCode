import pytest
from solutions.sol_1079 import Solution


cases = [
    {
        "input": {"tiles": "AAB"},
        "output": 8,
    },
    {
        "input": {"tiles": "AAABBC"},
        "output": 188,
    },
    {
        "input": {"tiles": "V"},
        "output": 1,
    },
]


@pytest.mark.sol1079
def test_run():
    for case in cases:
        assert (
            Solution.num_tile_possibilities(
                tiles=case["input"]["tiles"],
            )
            == case["output"]
        )
