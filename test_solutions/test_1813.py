import pytest
from solutions.sol_1813 import Solution


cases = [
    {
        "input": {"sentence1": "My name is Haley", "sentence2": "My Haley"},
        "output": True,
    },
    {
        "input": {"sentence1": "of", "sentence2": "A lot of words"},
        "output": False,
    },
    {
        "input": {"sentence1": "Eating right now", "sentence2": "Eating"},
        "output": True,
    },
]


@pytest.mark.sol1813
def test_run():
    for case in cases:
        assert (
            Solution.are_sentences_similar(
                sentence1=case["input"]["sentence1"],
                sentence2=case["input"]["sentence2"],
            )
            == case["output"]
        )
