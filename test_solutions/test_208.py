import pytest
from solutions.sol_208 import Trie

cases = [
    {
        'input': {
            'commands': ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            'args': [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        },
        'output': [None, None, True, False, True, None, True]
    },
]


@pytest.mark.sol208
def test_run():
    for case in cases:
        commands = case['input']['commands']
        args = case['input']['args']

        t = Trie()
        answer = [None]
        for i in range(1, len(commands)):
            if commands[i] == 'insert':
                t.insert(args[i][0])
                answer.append(None)
                continue
            if commands[i] == 'search':
                answer.append(t.search(args[i][0]))
                continue
            if commands[i] == 'startsWith':
                answer.append(t.startsWith(args[i][0]))

        assert answer == case['output']
