import pytest
from solutions.sol_705 import MyHashSet

cases = [
    {
        'input': {
            'commands': ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"],
            'args': [[], [1], [2], [1], [3], [2], [2], [2], [2]],
        },
        'output': [None, None, None, True, False, None, True, None, False],
    },
]


@pytest.mark.sol_705
def test_run():
    for case in cases:
        s = MyHashSet()
        commands = case['input']['commands'][1:]
        args = case['input']['args'][1:]
        result = [None]
        for i in range(len(commands)):
            cmd = commands[i]
            if cmd == 'add':
                result.append(s.add(args[i][0]))
            elif cmd == 'remove':
                result.append(s.remove(args[i][0]))
            else:
                result.append(s.contains(args[i][0]))
        assert result == case['output']
