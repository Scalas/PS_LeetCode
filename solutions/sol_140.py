from typing import List


class Solution:
    @staticmethod
    def word_break(s: str, word_dict: List[str]) -> List[str]:
        n = len(s)
        ws = set(word_dict)
        answer = []

        def dfs(cur, sentence_buffer):
            nonlocal n, answer
            if cur == n:
                sentence = "".join(sentence_buffer)
                words = sentence.split(" ")
                for word in words:
                    if word not in ws:
                        return
                answer.append(sentence)
                return
            sentence_buffer.append(s[cur])
            sentence_buffer.append(" ")
            dfs(cur + 1, sentence_buffer)
            sentence_buffer.pop()
            dfs(cur + 1, sentence_buffer)
            sentence_buffer.pop()

        dfs(0, [])
        return answer
