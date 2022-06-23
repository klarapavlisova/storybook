from .api import (
    Player,
    Effect,
)


class IncreaseBy(Effect):
    def __init__(self, attribute: str, value: int):
        self.attribute = attribute
        self.value = value

    def process(self, player: Player):
        player.story_attributes[self.attribute] += self.value
