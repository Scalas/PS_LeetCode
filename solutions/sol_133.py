class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    @staticmethod
    def clone_graph(node: "Node") -> "Node":
        clones = dict()

        def clone(target):
            if not target:
                return
            clone_node = Node(
                target.val, [neighbor.val for neighbor in target.neighbors]
            )
            clones[target.val] = clone_node
            for neighbor in target.neighbors:
                if neighbor.val in clones:
                    continue
                clone(neighbor)

        clone(node)

        for clone in clones.values():
            clone.neighbors = [clones[neighbor_id] for neighbor_id in clone.neighbors]

        return clones[node.val] if node else None
