class Node:
    def __init__(self, val="", is_term=False):
        self.__val = val
        self.__is_term = is_term
        self.__children = dict()

    def get_child(self, alpha):
        return self.__children.get(alpha, None)

    def add_child(self, child):
        self.__children[child.__val] = child

    def mark_terminal(self):
        self.__is_term = True

    def is_terminal(self):
        return self.__is_term


class Trie:
    def __init__(self):
        self.__root = Node()

    def insert(self, word) -> None:
        pos = self.__root
        idx = 0
        while idx < len(word):
            child = pos.get_child(word[idx])
            if not child:
                break
            pos = child
            idx += 1
        while idx < len(word):
            new_node = Node(word[idx], False)
            pos.add_child(new_node)
            pos = new_node
            idx += 1
        pos.mark_terminal()

    def search(self, word: str) -> bool:
        pos = self.__root
        for c in word:
            child = pos.get_child(c)
            if not child:
                return False
            pos = child
        return pos.is_terminal()

    def startsWith(self, prefix: str) -> bool:
        pos = self.__root
        for c in prefix:
            child = pos.get_child(c)
            if not child:
                return False
            pos = child
        return True
