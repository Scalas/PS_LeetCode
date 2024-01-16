import pytest
from solutions.sol_380 import RandomizedSet

cases = [
    {
        "input": {
            "commands": ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
            "args": [[], [1], [2], [2], [], [1], [2], []],
        },
        "output": [None, True, False, True, 2, True, False, 2],
    },
]


@pytest.mark.sol380
def test_run():
    for case in cases:
        commands = case["input"]["commands"]
        args = case["input"]["args"]
        output = case["output"]

        rs = RandomizedSet()
        for i in range(1, len(commands)):
            cmd = commands[i]
            arg = args[i]
            if cmd == "insert":
                assert output[i] == rs.insert(arg[0])
            elif cmd == "remove":
                assert output[i] == rs.remove(arg[0])
            else:
                while True:
                    if output[i] == rs.get_random():
                        break
