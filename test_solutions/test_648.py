import pytest
from solutions.sol_648 import Solution

cases = [
    {
        "input": {
            "dictionary": ["cat", "bat", "rat"],
            "sentence": "the cattle was rattled by the battery",
        },
        "output": "the cat was rat by the bat",
    },
    {
        "input": {
            "dictionary": ["a", "b", "c"],
            "sentence": "aadsfasf absbs bbab cadsfafs",
        },
        "output": "a a b c",
    },
]


@pytest.mark.sol_648
def test_run():
    for case in cases:
        assert (
            Solution.replace_words(
                dictionary=case["input"]["dictionary"],
                sentence=case["input"]["sentence"],
            )
            == case["output"]
        )
