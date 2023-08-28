import pytest
from solutions.sol_225 import MyStack

cases = [
    {
        "input": {
            "commands": [
                "MyStack",
                "push",
                "push",
                "top",
                "pop",
                "empty",
            ],
            "args": [[], [1], [2], [], [], []],
        },
        "output": [None, None, None, 2, 2, False],
    },
]


@pytest.mark.sol225
def test_run():
    for case in cases:
        commands = case["input"]["commands"]
        args = case["input"]["args"]

        s = MyStack()
        answer = [None]
        for i in range(1, len(commands)):
            if commands[i] == "push":
                s.push(args[i][0])
                answer.append(None)
                continue
            if commands[i] == "pop":
                answer.append(s.pop())
                continue
            if commands[i] == "top":
                answer.append(s.top())
                continue
            if commands[i] == "empty":
                answer.append(s.empty())
        assert answer == case["output"]
