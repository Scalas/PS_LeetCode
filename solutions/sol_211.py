class Node:
    def __init__(self, val="", is_term=False):
        self.__val = val
        self.__is_term = is_term
        self.__children = dict()

    def get_child(self, alpha):
        return self.__children.get(alpha, None)

    def get_children(self):
        return self.__children.values()

    def add_child(self, child):
        self.__children[child.__val] = child

    def mark_terminal(self):
        self.__is_term = True

    def is_terminal(self):
        return self.__is_term


class WordDictionary:
    def __init__(self):
        self.__root = Node()

    def addWord(self, word: str) -> None:
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
        return self.__search(self.__root, word, 0)

    def __search(self, node, word, idx):
        if idx == len(word):
            return node.is_terminal()
        if word[idx] == ".":
            for child in node.get_children():
                if self.__search(child, word, idx + 1):
                    return True
            return False
        else:
            child = node.get_child(word[idx])
            if not child:
                return False
            return self.__search(child, word, idx + 1)
