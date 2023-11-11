import pytest
from solutions.sol_2642 import Graph

cases = [
    {
        "input": {
            "command": [
                "Graph",
                "shortest_path",
                "shortest_path",
                "add_edge",
                "shortest_path",
            ],
            "args": [
                [4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]],
                [3, 2],
                [0, 3],
                [[1, 3, 4]],
                [0, 3],
            ],
        },
        "output": [None, 6, -1, None, 6],
    },
]


@pytest.mark.sol_2642
def test_run():
    for case in cases:
        commands = case["input"]["command"]
        args = case["input"]["args"]
        graph = Graph(args[0][0], args[0][1])
        result = [None]
        for i in range(1, len(commands)):
            arg = args[i]
            if commands[i] == "add_edge":
                result.append(graph.add_edge(arg[0]))
            else:
                result.append(graph.shortest_path(arg[0], arg[1]))
        assert result == case["output"]
