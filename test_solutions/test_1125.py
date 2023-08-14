import pytest
from solutions.sol_1125 import Solution

cases = [
    {
        "input": {
            "req_skills": ["java", "nodejs", "reactjs"],
            "people": [["java"], ["nodejs"], ["nodejs", "reactjs"]],
        },
        "output": [0, 2],
    },
    {
        "input": {
            "req_skills": ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
            "people": [
                ["algorithms", "math", "java"],
                ["algorithms", "math", "reactjs"],
                ["java", "csharp", "aws"],
                ["reactjs", "csharp"],
                ["csharp", "math"],
                ["aws", "java"],
            ],
        },
        "output": [1, 2],
    },
]


@pytest.mark.sol1125
def test_run():
    for case in cases:
        assert (
            Solution.smallest_sufficient_team(
                req_skills=case["input"]["req_skills"],
                people=case["input"]["people"],
            )
            == case["output"]
        )
