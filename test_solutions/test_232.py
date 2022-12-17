# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

import pytest
from solutions.sol_232 import MyQueue

cases = [
    {
        'input': {
            'commands': ["push", "push", "peek", "pop", "empty"],
            'args': [[1], [2], [None], [None], [None]]
        },
        'output': [None, None, 1, 1, False]
    },
]


@pytest.mark.sol232
def test_run():
    for case in cases:
        obj = MyQueue()
        commands = case['input']['commands']
        args = case['input']['args']
        result = []
        for i in range(len(commands)):
            command, arg = commands[i], args[i]
            if command == 'push':
                result.append(obj.push(arg[0]))
            elif command == 'pop':
                result.append(obj.pop())
            elif command == 'peek':
                result.append(obj.peek())
            elif command == 'empty':
                result.append(obj.empty())
        assert result == case['output']
