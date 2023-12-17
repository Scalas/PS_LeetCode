import pytest
from solutions.sol_2353 import FoodRatings

cases = [
    {
        "input": {
            "commands": [
                "FoodRatings",
                "highest_rated",
                "highest_rated",
                "change_rating",
                "highest_rated",
                "change_rating",
                "highest_rated",
            ],
            "args": [
                [
                    ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                    ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                    [9, 12, 8, 15, 14, 7],
                ],
                ["korean"],
                ["japanese"],
                ["sushi", 16],
                ["japanese"],
                ["ramen", 16],
                ["japanese"],
            ],
        },
        "output": [None, "kimchi", "ramen", None, "sushi", None, "ramen"],
    },
]


@pytest.mark.sol2353
def test_run():
    for case in cases:
        res = [None]
        ratings = FoodRatings(*case["input"]["args"][0])
        commands = case["input"]["commands"]
        args = case["input"]["args"]
        for i in range(1, len(commands)):
            cmd = commands[i]
            arg = args[i]
            if cmd == "change_rating":
                res.append(ratings.change_rating(*arg))
            elif cmd == "highest_rated":
                res.append(ratings.highest_rated(*arg))
        assert res == case["output"]
