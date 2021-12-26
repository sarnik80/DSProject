class Node:
    def __init__(self, person=None,children=None):
        self.__data = person
        self.__children = []

        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        assert isinstance(node, Node)
        self.__children.append(node)




