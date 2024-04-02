class Solution:
    @staticmethod
    def is_isomorphic(s: str, t: str) -> bool:
        mapping = dict()
        used = set()

        for i in range(len(s)):
            u, v = s[i], t[i]
            target = mapping.get(u, None)
            if target:
                if target != v:
                    return False
                else:
                    continue
            if v in used:
                return False
            used.add(v)
            mapping[u] = v
        return True
