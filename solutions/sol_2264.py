class Solution:
    @staticmethod
    def largest_good_integer(num: str) -> str:
        pre = num[0]
        cnt = 1
        answer = ""
        for d in num[1:]:
            if d == pre:
                cnt += 1
            else:
                if cnt >= 3 and pre > answer:
                    answer = pre
                pre, cnt = d, 1
        if cnt >= 3 and pre >= answer:
            answer = pre
        return answer * 3
