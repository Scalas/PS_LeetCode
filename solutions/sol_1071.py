class Solution:
    @staticmethod
    def gcd_of_strings(str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        while str1:
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    return ""
            str2 = str2[len(str1) :]
            if len(str1) > len(str2):
                str1, str2 = str2, str1
        return str2
