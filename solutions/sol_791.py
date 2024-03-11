class Solution:
    @staticmethod
    def custom_sort_string(order: str, s: str) -> str:
        index = dict()
        for i in range(len(order)):
            index[order[i]] = i
        return "".join(sorted(s, key=lambda x: index.get(x, 999)))
