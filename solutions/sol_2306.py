from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def distinct_names(ideas: List[str]) -> int:
        category = dict()
        id_no = 0
        banned = defaultdict(set)
        postfix = [[] for _ in range(26)]
        idea_meta = []
        for idea in ideas:
            key = idea[1:]
            if key not in category:
                category[key] = id_no
                id_no += 1
            id = category[key]
            alpha = ord(idea[0]) - ord("a")
            banned[id].add(alpha)
            postfix[alpha].append(id)
            idea_meta.append((alpha, id))

        alpha_count = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for pid in postfix[i]:
                for j in range(26):
                    if j not in banned[pid]:
                        alpha_count[i][j] += 1

        answer = 0
        for alpha, id in idea_meta:
            for i in range(26):
                if i in banned[id]:
                    continue
                answer += alpha_count[i][alpha]
        return answer
