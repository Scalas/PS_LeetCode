import pytest
from solutions.sol_472 import Solution

cases = [
    {
        "input": {
            "words": [
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat",
            ]
        },
        "output": ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
    },
    {"input": {"words": ["cat", "dog", "catdog"]}, "output": ["catdog"]},
]


@pytest.mark.sol_472
def test_run():
    for case in cases:
        assert sorted(
            Solution.find_all_concatenated_words_in_a_dict(words=case["input"]["words"])
        ) == sorted(case["output"])
