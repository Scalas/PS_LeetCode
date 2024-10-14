import pytest
from solutions.sol_432 import AllOne

cases = [
    {
        "input": {
            "commands": [
                "AllOne",
                "inc",
                "inc",
                "getMaxKey",
                "getMinKey",
                "inc",
                "getMaxKey",
                "getMinKey",
            ],
            "args": [[], ["hello"], ["hello"], [], [], ["leet"], [], []],
        },
        "output": [None, None, None, "hello", "hello", None, "hello", "leet"],
    },
]


@pytest.mark.sol432
def test_run():
    for case in cases:
        commands = case["input"]["commands"]
        args = case["input"]["args"]
        ao = AllOne()
        res = [None]
        for i in range(1, len(commands)):
            cmd = commands[i]
            if cmd == "inc":
                res.append(ao.inc(args[i][0]))
            elif cmd == "dec":
                res.append(ao.dec(args[i][0]))
            elif cmd == "getMaxKey":
                res.append(ao.get_max_key())
            else:
                res.append(ao.get_min_key())
        assert res == case["output"]
