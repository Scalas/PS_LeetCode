import pytest
from solutions.sol_641 import MyCircularDeque

cases = [
    {
        "input": {
            "commands": [
                "MyCircularDeque",
                "insertLast",
                "insertLast",
                "insertFront",
                "insertFront",
                "getRear",
                "isFull",
                "deleteLast",
                "insertFront",
                "getFront",
            ],
            "args": [[3], [1], [2], [3], [4], [], [], [], [4], []],
        },
        "output": [None, True, True, True, False, 2, True, True, True, 4],
    },
]


@pytest.mark.sol432
def test_run():
    for case in cases:
        commands = case["input"]["commands"]
        args = case["input"]["args"]
        q = MyCircularDeque(args[0][0])
        res = [None]
        for i in range(1, len(commands)):
            cmd = commands[i]
            if cmd == "insertLast":
                res.append(q.insert_last(args[i][0]))
            elif cmd == "insertFront":
                res.append(q.insert_front(args[i][0]))
            elif cmd == "deleteLast":
                res.append(q.delete_last())
            elif cmd == "deleteFront":
                res.append(q.delete_front())
            elif cmd == "getFront":
                res.append(q.get_front())
            elif cmd == "getRear":
                res.append(q.get_rear())
            elif cmd == "isEmpty":
                res.append(q.is_empty())
            else:
                res.append(q.is_full())
        assert res == case["output"]
