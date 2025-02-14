import pytest
from solutions.sol_1352 import ProductOfNumbers

cases = [
    {
        "input": {
            "command": [
                "ProductOfNumbers",
                "add",
                "add",
                "add",
                "add",
                "add",
                "get_product",
                "get_product",
                "get_product",
                "add",
                "get_product",
            ],
            "args": [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]],
        },
        "output": [None, None, None, None, None, None, 20, 40, 0, None, 32],
    },
    {
        "input": {
            "command": [
                "ProductOfNumbers",
                "add",
                "get_product",
                "get_product",
                "add",
                "add",
                "get_product",
                "add",
                "get_product",
                "add",
                "get_product",
                "add",
                "get_product",
                "get_product",
                "add",
                "get_product",
            ],
            "args": [
                [],
                [7],
                [1],
                [1],
                [4],
                [5],
                [3],
                [4],
                [4],
                [3],
                [4],
                [8],
                [1],
                [6],
                [2],
                [3],
            ],
        },
        "output": [
            None,
            None,
            7,
            7,
            None,
            None,
            140,
            None,
            560,
            None,
            240,
            None,
            8,
            13440,
            None,
            48,
        ],
    },
]


@pytest.mark.sol_1352
def test_run():
    for case in cases:
        args = case["input"]["args"]
        commands = case["input"]["command"]
        pon = ProductOfNumbers()
        result = [None]
        for i in range(1, len(commands)):
            cmd, arg = commands[i], args[i]
            if cmd == "add":
                result.append(pon.add(arg[0]))
            else:
                result.append(pon.get_product(arg[0]))
        assert result == case["output"]
