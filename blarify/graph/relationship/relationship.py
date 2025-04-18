from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from blarify.graph.node import Node
    from blarify.graph.relationship import RelationshipType


class Relationship:
    start_node: "Node"
    end_node: "Node"
    rel_type: "RelationshipType"
    scope_text: str

    def __init__(self, start_node: "Node", end_node: "Node", rel_type: "RelationshipType", scope_text: str = ""):
        self.start_node = start_node
        self.end_node = end_node
        self.rel_type = rel_type
        self.scope_text = scope_text

    def as_object(self) -> dict:
        return {
            "sourceId": self.start_node.hashed_id,
            "targetId": self.end_node.hashed_id,
            "type": self.rel_type.name,
            "scopeText": self.scope_text,
        }

    def __str__(self) -> str:
        return f"{self.start_node} --[{self.rel_type}]-> {self.end_node}"
