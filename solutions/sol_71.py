class Solution:
    @staticmethod
    def simplify_path(path: str) -> str:
        path_steps = path.split('/')
        path_st = []

        for nxt in path_steps:
            if nxt == '' or nxt == '.':
                continue
            if nxt == '..':
                if path_st:
                    path_st.pop()
            else:
                path_st.append(nxt)

        return '/' + '/'.join(path_st)
