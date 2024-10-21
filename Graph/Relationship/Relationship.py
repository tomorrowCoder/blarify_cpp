from Graph.Relationship import RelationshipType
from Graph.Node import Node


class Relationship:
    def __init__(self, start_node: Node, end_node: Node, rel_type: RelationshipType):
        self.start_node = start_node
        self.end_node = end_node
        self.rel_type = rel_type

    def __str__(self):
        return f"{self.start_node} --[{self.rel_type}]-> {self.end_node}"
