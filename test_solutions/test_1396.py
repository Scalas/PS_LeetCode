import pytest

from solutions.sol_1396 import UndergroundSystem

cases = [
    {
        "input": {
            "commands": [
                "UndergroundSystem",
                "checkIn",
                "checkIn",
                "checkIn",
                "checkOut",
                "checkOut",
                "checkOut",
                "getAverageTime",
                "getAverageTime",
                "checkIn",
                "getAverageTime",
                "checkOut",
                "getAverageTime",
            ],
            "args": [
                [],
                [45, "Leyton", 3],
                [32, "Paradise", 8],
                [27, "Leyton", 10],
                [45, "Waterloo", 15],
                [27, "Waterloo", 20],
                [32, "Cambridge", 22],
                ["Paradise", "Cambridge"],
                ["Leyton", "Waterloo"],
                [10, "Leyton", 24],
                ["Leyton", "Waterloo"],
                [10, "Waterloo", 38],
                ["Leyton", "Waterloo"],
            ],
        },
        "output": [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            14.00000,
            11.00000,
            None,
            11.00000,
            None,
            12.00000,
        ],
    },
    {
        "input": {
            "commands": [
                "UndergroundSystem",
                "checkIn",
                "checkOut",
                "getAverageTime",
                "checkIn",
                "checkOut",
                "getAverageTime",
                "checkIn",
                "checkOut",
                "getAverageTime",
            ],
            "args": [
                [],
                [10, "Leyton", 3],
                [10, "Paradise", 8],
                ["Leyton", "Paradise"],
                [5, "Leyton", 10],
                [5, "Paradise", 16],
                ["Leyton", "Paradise"],
                [2, "Leyton", 21],
                [2, "Paradise", 30],
                ["Leyton", "Paradise"],
            ],
        },
        "output": [None, None, None, 5.00000, None, None, 5.50000, None, None, 6.66667],
    },
]


@pytest.mark.sol1396
def test_run():
    for case in cases:
        commands = case["input"]["commands"][1:]
        args = case["input"]["args"][1:]
        result = [None]
        system = UndergroundSystem()
        for i in range(len(commands)):
            cmd = commands[i]
            if cmd == "checkIn":
                result.append(system.check_in(*args[i]))
            elif cmd == "checkOut":
                result.append(system.check_out(*args[i]))
            else:
                result.append(round(system.get_average_time(*args[i]), 5))
        assert result == case["output"]
