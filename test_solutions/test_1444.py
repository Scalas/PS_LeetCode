import pytest
from solutions.sol_1444 import Solution

cases = [
    {
        "input": {
            "pizza": ["A..", "AAA", "..."],
            "k": 3,
        },
        "output": 3,
    },
    {
        "input": {
            "pizza": ["A..", "AA.", "..."],
            "k": 3,
        },
        "output": 1,
    },
    {
        "input": {
            "pizza": ["A..", "A..", "..."],
            "k": 1,
        },
        "output": 1,
    },
    {
        "input": {
            "pizza": [
                "..A.A.AAA...AAAAAA.AA..A..A.A......A.AAA.AAAAAA.AA",
                "A.AA.A.....AA..AA.AA.A....AAA.A........AAAAA.A.AA.",
                "A..AA.AAA..AAAAAAAA..AA...A..A...A..AAA...AAAA..AA",
                "....A.A.AA.AA.AA...A.AA.AAA...A....AA.......A..AA.",
                "AAA....AA.A.A.AAA...A..A....A..AAAA...A.A.A.AAAA..",
                "....AA..A.AA..A.A...A.A..AAAA..AAAA.A.AA..AAA...AA",
                "A..A.AA.AA.A.A.AA..A.A..A.A.AAA....AAAAA.A.AA..A.A",
                ".AA.A...AAAAA.A..A....A...A.AAAA.AA..A.AA.AAAA.AA.",
                "A.AA.AAAA.....AA..AAA..AAAAAAA...AA.A..A.AAAAA.A..",
                "A.A...A.A...A..A...A.AAAA.A..A....A..AA.AAA.AA.AA.",
                ".A.A.A....AAA..AAA...A.AA..AAAAAAA.....AA....A....",
                "..AAAAAA..A..A...AA.A..A.AA......A.AA....A.A.AAAA.",
                "...A.AA.AAA.AA....A..AAAA...A..AAA.AAAA.A.....AA.A",
                "A.AAAAA..A...AAAAAAAA.AAA.....A.AAA.AA.A..A.A.A...",
                "A.A.AA...A.A.AA...A.AA.AA....AA...AA.A..A.AA....AA",
                "AA.A..A.AA..AAAAA...A..AAAAA.AA..AA.AA.A..AAAAA..A",
                "...AA....AAAA.A...AA....AAAAA.A.AAAA.A.AA..AA..AAA",
                "..AAAA..AA..A.AA.A.A.AA...A...AAAAAAA..A.AAA..AA.A",
                "AA....AA....AA.A......AAA...A...A.AA.A.AA.A.A.AA.A",
                "A.AAAA..AA..A..AAA.AAA.A....AAA.....A..A.AA.A.A...",
                "..AA...AAAAA.A.A......AA...A..AAA.AA..A.A.A.AA..A.",
                ".......AA..AA.AAA.A....A...A.AA..A.A..AAAAAAA.AA.A",
                ".A.AAA.AA..A.A.A.A.A.AA...AAAA.A.A.AA..A...A.AAA..",
                "A..AAAAA.A..A..A.A..AA..A...AAA.AA.A.A.AAA..A.AA..",
                "A.AAA.A.AAAAA....AA..A.AAA.A..AA...AA..A.A.A.AA.AA",
                ".A..AAAA.A.A.A.A.......AAAA.AA...AA..AAA..A...A.AA",
                "A.A.A.A..A...AA..A.AAA..AAAAA.AA.A.A.A..AA.A.A....",
                "A..A..A.A.AA.A....A...A......A.AA.AAA..A.AA...AA..",
                ".....A..A...A.A...A..A.AA.A...AA..AAA...AA..A.AAA.",
                "A...AA..A..AA.A.A.AAA..AA..AAA...AAA..AAA.AAAAA...",
                "AA...AAA.AAA...AAAA..A...A..A...AA...A..AA.A...A..",
                "A.AA..AAAA.AA.AAA.A.AA.A..AAAAA.A...A.A...A.AA....",
                "A.......AA....AA..AAA.AAAAAAA.A.AA..A.A.AA....AA..",
                ".A.A...AA..AA...AA.AAAA.....A..A..A.AA.A.AA...A.AA",
                "..AA.AA.AA..A...AA.AA.AAAAAA.....A.AA..AA......A..",
                "AAA..AA...A....A....AA.AA.AA.A.A.A..AA.AA..AAA.AAA",
                "..AAA.AAA.A.AA.....AAA.A.AA.AAAAA..AA..AA.........",
                ".AA..A......A.A.AAA.AAAA...A.AAAA...AAA.AAAA.....A",
                "AAAAAAA.AA..A....AAAA.A..AA.A....AA.A...A.A....A..",
                ".A.A.AA..A.AA.....A.A...A.A..A...AAA..A..AA..A.AAA",
                "AAAA....A...A.AA..AAA..A.AAA..AA.........AA.AAA.A.",
                "......AAAA..A.AAA.A..AAA...AAAAA...A.AA..A.A.AA.A.",
                "AA......A.AAAAAAAA..A.AAA...A.A....A.AAA.AA.A.AAA.",
                ".A.A....A.AAA..A..AA........A.AAAA.AAA.AA....A..AA",
                ".AA.A...AA.AAA.A....A.A...A........A.AAA......A...",
                "..AAA....A.A...A.AA..AAA.AAAAA....AAAAA..AA.AAAA..",
                "..A.AAA.AA..A.AA.A...A.AA....AAA.A.....AAA...A...A",
                ".AA.AA...A....A.AA.A..A..AAA.A.A.AA.......A.A...A.",
                "...A...A.AA.A..AAAAA...AA..A.A..AAA.AA...AA...A.A.",
                "..AAA..A.A..A..A..AA..AA...A..AA.AAAAA.A....A..A.A",
            ],
            "k": 8,
        },
        "output": 641829390,
    },
]


@pytest.mark.sol1444
def test_run():
    for case in cases:
        assert (
            Solution.ways(
                pizza=case["input"]["pizza"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
