import pytest
from solutions.sol_706 import MyHashMap

cases = [
    {
        "input": {
            "commands": [
                "MyHashMap",
                "put",
                "put",
                "get",
                "get",
                "put",
                "get",
                "remove",
                "get",
            ],
            "args": [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
        },
        "output": [None, None, None, 1, -1, None, 1, None, -1],
    },
]


@pytest.mark.sol_706
def test_run():
    for case in cases:
        m = MyHashMap()
        commands = case["input"]["commands"][1:]
        args = case["input"]["args"][1:]
        result = [None]
        for i in range(len(commands)):
            cmd = commands[i]
            if cmd == "put":
                result.append(m.put(args[i][0], args[i][1]))
            elif cmd == "remove":
                result.append(m.remove(args[i][0]))
            else:
                result.append(m.get(args[i][0]))
        assert result == case["output"]
