import pytest
from solutions.sol_93 import Solution

cases = [
    {"input": {"s": "25525511135"}, "output": ["255.255.11.135", "255.255.111.35"]},
    {"input": {"s": "0000"}, "output": ["0.0.0.0"]},
    {
        "input": {"s": "101023"},
        "output": ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"],
    },
]


@pytest.mark.sol93
def test_run():
    for case in cases:
        assert Solution.restore_ip_addresses(s=case["input"]["s"]) == case["output"]
