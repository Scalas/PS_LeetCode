import pytest
from solutions.sol_731 import MyCalendarTwo

cases = [
    {
        "input": {
            "commands": [
                "MyCalendarTwo",
                "book",
                "book",
                "book",
                "book",
                "book",
                "book",
            ],
            "args": [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
        },
        "output": [None, True, True, True, False, True, True],
    },
]


@pytest.mark.sol731
def test_run():
    for case in cases:
        commands = case["input"]["commands"]
        args = case["input"]["args"]
        q = MyCalendarTwo()
        res = [None]
        for i in range(1, len(commands)):
            res.append(q.book(args[i][0], args[i][1]))
        assert res == case["output"]
