class Solution:
    @staticmethod
    def merge_alternately(word1: str, word2: str) -> str:
        st = []
        n, m = len(word1), len(word2)
        for i in range(max(n, m)):
            if i < n:
                st.append(word1[i])
            if i < m:
                st.append(word2[i])
        return ''.join(st)
