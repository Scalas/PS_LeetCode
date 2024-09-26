import pytest
from solutions.sol_729 import MyCalendar


cases = [
    {
        "input": {"book": [[10, 20], [15, 25], [20, 30]]},
        "output": [True, False, True],
    },
]


@pytest.mark.sol729
def test_run():
    for case in cases:
        cal = MyCalendar()
        res = []
        for u, v in case["input"]["book"]:
            res.append(cal.book(u, v))
        assert res == case["output"]
