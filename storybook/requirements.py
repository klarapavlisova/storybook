from .api import (
    Player,
    Requirement,
)


class Comparison(Requirement):
    def __init__(self, attribute, value):
        self.attribute: str = attribute
        self.value: int = value


class EqualsTo(Comparison):
    def process(self, player: Player) -> bool:
        return player.story_attributes[self.attribute] == self.value


class GreaterThan(Comparison):
    def process(self, player: Player) -> bool:
        return player.story_attributes[self.attribute] > self.value


class LesserThan(Comparison):
    def process(self, player: Player) -> bool:
        return player.story_attributes[self.attribute] < self.value
