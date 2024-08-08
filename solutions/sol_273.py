class Solution:
    @staticmethod
    def number_to_words(num: int) -> str:
        if num == 0:
            return "Zero"

        one = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        before_twenty = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        deca = [
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        unit = ["", "Thousand", "Million", "Billion"]

        def create(d100, d10, d1, cu):
            res = []
            if d100 > 0:
                res.append(one[d100])
                res.append("Hundred")
            if d10 == 0:
                if d1 > 0:
                    res.append(one[d1])
            elif d10 == 1:
                res.append(before_twenty[d1])
            else:
                res.append(deca[d10 - 2])
                if d1 > 0:
                    res.append(one[d1])
            if not res:
                return ""
            res.append(unit[cu])
            return " ".join(res)

        s = str(num)
        n = len(s)
        u = 0
        answer = []
        last = len(s)
        for i in range(n - 3, -1, -3):
            r = create(int(s[i]), int(s[i + 1]), int(s[i + 2]), u)
            if r:
                answer.append(r)
            last = i
            u += 1
        if last > 0:
            r = create(
                0,
                0 if last == 1 else int(s[0]),
                int(s[0]) if last == 1 else int(s[1]),
                u,
            )
            if r:
                answer.append(r)
        return " ".join(answer[::-1]).strip()
