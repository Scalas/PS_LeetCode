import pytest
from solutions.sol_146 import LRUCache

cases = [
    {
        'input': {
            'commands': ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            'args': [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
        },
        'output': [None, None, None, 1, None, -1, None, -1, 3, 4]
    },
    {
        'input': {
            'commands': ["LRUCache", "put", "put", "get", "put", "put", "get"],
            'args': [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]],
        },
        'output': [None, None, None, 2, None, None, -1]
    },
    {
        'input': {
            'commands':
                ["LRUCache", "put", "put", "put", "put", "get", "get"],
            'args': [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]],
        },
        'output': [None, None, None, None, None, -1, 3]
    },
]


@pytest.mark.sol146
def test_run():
    for case in cases:
        commands = case['input']['commands']
        args = case['input']['args']
        cache = LRUCache(capacity=args[0][0])
        res = [None]
        for cmd, arg in zip(commands[1:], args[1:]):
            if cmd == 'put':
                res.append(cache.put(arg[0], arg[1]))
            elif cmd == 'get':
                res.append(cache.get(arg[0]))
        assert res == case['output']
