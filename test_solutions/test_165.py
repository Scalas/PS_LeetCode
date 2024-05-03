import pytest

from solutions.sol_165 import Solution

cases = [
    {
        "input": {
            "version1": "1.01",
            "version2": "1.001",
        },
        "output": 0,
    },
    {
        "input": {
            "version1": "1.0",
            "version2": "1.0.0",
        },
        "output": 0,
    },
    {
        "input": {
            "version1": "0.1",
            "version2": "1.1",
        },
        "output": -1,
    },
    {
        "input": {
            "version1": "1.0",
            "version2": "1",
        },
        "output": 0,
    },
    {
        "input": {
            "version1": "1.0.2.0",
            "version2": "1.0.2",
        },
        "output": 0,
    },
]


@pytest.mark.sol165
def test_run():
    for case in cases:
        assert (
            Solution.compare_version(
                version1=case["input"]["version1"],
                version2=case["input"]["version2"],
            )
            == case["output"]
        )
