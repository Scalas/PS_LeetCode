import pytest
from solutions.sol_1472 import BrowserHistory

cases = [
    {
        'input': {
            'commands': ["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward",
                         "back", "back"],
            'args': [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1],
                     ["linkedin.com"], [2], [2], [7]],
        },
        'output': [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com",
                   "google.com", "leetcode.com"]
    },
]


@pytest.mark.sol1472
def test_run():
    for case in cases:
        commands = case['input']['commands']
        args = case['input']['args']

        browser_history = BrowserHistory(args[0][0])
        answer = [None]
        for i in range(1, len(commands)):
            if commands[i] == 'visit':
                browser_history.visit(args[i][0])
                answer.append(None)
                continue
            if commands[i] == 'back':
                answer.append(browser_history.back(int(args[i][0])))
                continue
            if commands[i] == 'forward':
                answer.append(browser_history.forward(int(args[i][0])))

        assert answer == case['output']
