import pytest
from solutions.sol_2101 import Solution

cases = [
    {
        'input': {
            'bombs': [[2,1,3],[6,1,4]],
        },
        'output': 2,
    },
    {
        'input': {
            'bombs': [[1,1,5],[10,10,5]],
        },
        'output': 1,
    },
    {
        'input': {
            'bombs': [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]],
        },
        'output': 5,
    },
    {
        'input': {
            'bombs': [[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]],
        },
        'output': 9,
    },
]


@pytest.mark.sol_2101
def test_run():
    for case in cases:
        assert Solution.maximum_detonation(
            bombs=case['input']['bombs'],
        ) == case['output']
