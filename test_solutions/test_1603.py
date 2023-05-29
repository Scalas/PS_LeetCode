import pytest
from solutions.sol_1603 import ParkingSystem

cases = [
    {
        'input': {
            'commands': ['ParkingSystem', 'addCar', 'addCar', 'addCar', 'addCar'],
            'args': [[1, 1, 0], [1], [2], [3], [1]],
        },
        'output': [None, True, True, False, False],
    },
]


@pytest.mark.sol1603
def test_run():
    for case in cases:
        res = [None]
        args = case['input']['args']
        ps = ParkingSystem(*args[0])
        for arg in args[1:]:
            res.append(ps.add_car(arg[0]))
        assert res == case['output']

