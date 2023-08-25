from typing import List


class Solution:
    @staticmethod
    def full_justify(words: List[str], max_width: int) -> List[str]:
        answer = []
        line = []
        space = 0
        for word in words:
            if not line:
                line.append(word)
                space += len(word)
                continue

            # non-first words occupy len(word) + 1 space
            if space + len(word) + 1 <= max_width:
                line.append(word)
                space += len(word) + 1
                continue

            cluster = len(line) - 1
            buf = [line[0]]
            required_whitespace = max_width - sum(map(lambda x: len(x), line))

            if cluster > 0:
                q = required_whitespace // cluster
                r = required_whitespace % cluster

                for w in line[1:]:
                    ws = q
                    if r:
                        ws += 1
                        r -= 1
                    buf.append(" " * ws)
                    buf.append(w)
            else:
                buf.append(" " * required_whitespace)
            answer.append("".join(buf))
            line = [word]
            space = len(word)

        last_line = " ".join(line)
        last_line += " " * (max_width - len(last_line))
        answer.append(last_line)

        return answer
