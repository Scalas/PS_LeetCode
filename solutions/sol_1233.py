from typing import List


class Solution:
    @staticmethod
    def remove_sub_folders(folder: List[str]) -> List[str]:
        root = dict()
        folder.sort(reverse=True)
        for path in folder:
            wd = root
            directories = path.split("/")
            for i in range(1, len(directories)):
                d = directories[i]
                if d not in wd:
                    wd[d] = [dict(), False]
                if i == len(directories) - 1:
                    wd[d][1] = True
                wd = wd[d][0]

        answer = []

        def dfs(cur, buf):
            nonlocal answer
            cd, is_term = cur
            if is_term or not cd:
                answer.append("/".join(buf))
                return

            for key in cd:
                buf.append(key)
                dfs(cd[key], buf)
                buf.pop()

        dfs([root, False], [""])
        return answer
