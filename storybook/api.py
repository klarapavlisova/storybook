class Player:
    current_page_id: str
    character_attributes: dict[str, str]
    story_attributes: dict[str, int]


class Effect:
    def process(self, player: Player):
        raise NotImplementedError()


class Requirement:
    def process(self, player: Player) -> bool:
        raise NotImplementedError()


class Choice:
    content: str
    requirements: list[Requirement]
    effects: list[Effect]
    next_page_id: str

    def is_available(self, player: Player) -> bool:
        return all(requirement.process(player) for requirement in self.requirements)

    def apply_choice(self, player: Player):
        for effect in self.effects:
            effect.process(player)

        player.current_page_id = self.next_page_id


class Page:
    id: str
    title: str
    content: str
    choices: list[Choice]


class Book:
    pages: dict[str, Page]
