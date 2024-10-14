import pytest
from solutions.sol_1381 import CustomStack

cases = [
    {
        "input": {
            "commands": [
                "CustomStack",
                "push",
                "push",
                "pop",
                "push",
                "push",
                "push",
                "increment",
                "increment",
                "pop",
                "pop",
                "pop",
                "pop",
            ],
            "args": [
                [3],
                [1],
                [2],
                [],
                [2],
                [3],
                [4],
                [5, 100],
                [2, 100],
                [],
                [],
                [],
                [],
            ],
        },
        "output": [
            None,
            None,
            None,
            2,
            None,
            None,
            None,
            None,
            None,
            103,
            202,
            201,
            -1,
        ],
    },
]


@pytest.mark.sol1381
def test_run():
    for case in cases:
        commands = case["input"]["commands"]
        args = case["input"]["args"]
        st = CustomStack(args[0][0])
        res = [None]
        for i in range(1, len(commands)):
            cmd = commands[i]
            if cmd == "push":
                res.append(st.push(args[i][0]))
            elif cmd == "increment":
                res.append(st.increment(args[i][0], args[i][1]))
            else:
                res.append(st.pop())
        assert res == case["output"]
