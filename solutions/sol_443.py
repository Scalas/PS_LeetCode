from typing import List


class Solution:
    @staticmethod
    def compress(chars: List[str]) -> int:
        comp = []
        ch, count = '', 0
        for c in chars:
            if c != ch:
                if count > 1:
                    comp.append(f'{ch}{count}')
                elif count == 1:
                    comp.append(f'{ch}')
                ch, count = c, 1
            else:
                count += 1
        if count > 1:
            comp.append(f'{ch}{count}')
        elif count == 1:
            comp.append(f'{ch}')

        compressed = ''.join(comp)
        for i in range(len(compressed)):
            chars[i] = compressed[i]
        return len(compressed)
