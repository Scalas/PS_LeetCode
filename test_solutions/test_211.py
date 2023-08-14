import pytest
from solutions.sol_211 import WordDictionary

cases = [
    {
        "input": {
            "commands": [
                "WordDictionary",
                "addWord",
                "addWord",
                "addWord",
                "search",
                "search",
                "search",
                "search",
            ],
            "args": [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
        },
        "output": [None, None, None, None, False, True, True, True],
    },
]


@pytest.mark.sol211
def test_run():
    for case in cases:
        commands = case["input"]["commands"]
        args = case["input"]["args"]

        w = WordDictionary()
        answer = [None]
        for i in range(1, len(commands)):
            if commands[i] == "addWord":
                w.addWord(args[i][0])
                answer.append(None)
                continue
            if commands[i] == "search":
                answer.append(w.search(args[i][0]))
                continue

        assert answer == case["output"]
