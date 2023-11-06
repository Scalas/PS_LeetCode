import pytest
from solutions.sol_1845 import SeatManager

cases = [
    {
        "input": {
            "commands": [
                "SeatManager",
                "reserve",
                "reserve",
                "unreserve",
                "reserve",
                "reserve",
                "reserve",
                "reserve",
                "unreserve",
            ],
            "args": [[5], [], [], [2], [], [], [], [], [5]],
        },
        "output": [None, 1, 2, None, 2, 3, 4, 5, None],
    },
]


@pytest.mark.sol1845
def test_run():
    for case in cases:
        res = [None]
        manager = SeatManager(case["input"]["args"][0][0])
        commands = case["input"]["commands"]
        args = case["input"]["args"]
        for i in range(1, len(commands)):
            cmd = commands[i]
            arg = args[i]
            if cmd == "reserve":
                res.append(manager.reserve())
            else:
                res.append(manager.unreserve(arg[0]))
        assert res == case["output"]
