from typing import List


class Solution:
    @staticmethod
    def asteroid_collision(asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            destroyed = False
            while st:
                if st[-1] * ast > 0:
                    break
                if ast > 0:
                    break
                u, v = abs(st[-1]), abs(ast)
                if u <= v:
                    st.pop()
                if u >= v:
                    destroyed = True
                    break
            if not destroyed:
                st.append(ast)
        return st
