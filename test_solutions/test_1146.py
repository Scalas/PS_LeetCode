import pytest
from solutions.sol_1146 import SnapshotArray

cases = [
    {
        "input": {
            "commands": ["SnapshotArray", "set", "snap", "set", "get"],
            "args": [[3], [0, 5], [], [0, 6], [0, 0]],
        },
        "output": [None, None, 0, None, 5],
    },
]


@pytest.mark.sol1146
def test_run():
    for case in cases:
        commands = case["input"]["commands"]
        args = case["input"]["args"]

        sa = SnapshotArray(args[0][0])
        res = [None]
        for i in range(1, len(commands)):
            cmd = commands[i]
            arg = args[i]
            if cmd == "set":
                res.append(sa.set(arg[0], arg[1]))
            elif cmd == "snap":
                res.append(sa.snap())
            else:
                res.append(sa.get(arg[0], arg[1]))
        assert res == case["output"]
