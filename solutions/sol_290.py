class Solution:
    @staticmethod
    def word_pattern(pattern: str, s: str) -> bool:
        words = s.split()
        n = len(words)
        if n != len(pattern):
            return False
        wk = dict()
        kw = dict()
        for i in range(len(words)):
            word, word_key = words[i], pattern[i]
            if word not in wk:
                if word_key in kw:
                    return False
                wk[word] = word_key
                kw[word_key] = word
            if wk[word] != word_key or kw[word_key] != word:
                return False
        return True


