import pytest
from solutions.sol_460 import LFUCache

cases = [
    {
        'input': {
            'commands': ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
            'args': [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
        },
        'output': [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
    },
    {
        'input': {
            'commands': ["LFUCache", "put", "put", "put", "put", "get", "get"],
            'args': [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
        },
        'output': [None, None, None, None, None, -1, 3]
    },
    {
        'input': {
            'commands': ["LFUCache", "put", "put", "get", "get", "put", "get", "get", "get"],
            'args': [[2], [2, 1], [3, 2], [3], [2], [4, 3], [2], [3], [4]]
        },
        'output': [None, None, None, 2, 1, None, 1, -1, 3]
    },
]


@pytest.mark.sol460
def test_run():
    for case in cases:
        commands = case['input']['commands']
        args = case['input']['args']
        obj = LFUCache(args[0][0])
        result = []
        for i in range(len(commands)):
            command, arg = commands[i], args[i]
            if command == 'put':
                result.append(obj.put(arg[0], arg[1]))
            elif command == 'get':
                result.append(obj.get(arg[0]))
            else:
                result.append(None)
        assert result == case['output']
