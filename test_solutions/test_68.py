import pytest
from solutions.sol_68 import Solution

cases = [
    {
        "input": {
            "words": ["This", "is", "an", "example", "of", "text", "justification."],
            "max_width": 16,
        },
        "output": ["This    is    an", "example  of text", "justification.  "],
    },
    {
        "input": {
            "words": ["What", "must", "be", "acknowledgment", "shall", "be"],
            "max_width": 16,
        },
        "output": ["What   must   be", "acknowledgment  ", "shall be        "],
    },
    {
        "input": {
            "words": [
                "Science", "is", "what", "we",
                "understand", "well", "enough",
                "to", "explain", "to", "a", "computer.",
                "Art", "is", "everything", "else", "we", "do",
            ],
            "max_width": 20,
        },
        "output": [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ],
    },
]


@pytest.mark.sol68
def test_run():
    for case in cases:
        assert (
            Solution.full_justify(
                words=case["input"]["words"], max_width=case["input"]["max_width"]
            )
            == case["output"]
        )
