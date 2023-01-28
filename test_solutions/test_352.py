import pytest
from solutions.sol_352 import SummaryRanges

cases = [
    {
        'input': {
            'commands': ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"],
            'args': [[None], [1], [None], [3], [None], [7], [None], [2], [None], [6], [None]]
        },
        'output': [None, None, [[1, 1]], None, [[1, 1], [3, 3]], None, [[1, 1], [3, 3], [7, 7]], None, [[1, 3], [7, 7]], None, [[1, 3], [6, 7]]]
    },
]


@pytest.mark.sol352
def test_run():
    for case in cases:
        obj = SummaryRanges()
        commands = case['input']['commands']
        args = case['input']['args']
        result = []
        for i in range(len(commands)):
            command, arg = commands[i], args[i]
            if command == 'addNum':
                result.append(obj.add_num(arg[0]))
            elif command == 'getIntervals':
                result.append(list(map(list, obj.get_intervals())))
            else:
                result.append(None)
        assert result == case['output']
