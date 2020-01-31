from attr import attrs

from .item_modifier import ItemModifier


@attrs(auto_attribs=True)
class Item:
    rarity: str = 'Rare'
    name: str = 'Pseudo'
    base: str = 'Pseudo'

    quality: int = 0
    # TODO: handle base stats
    stats: [str] = []

    raw_sockets: str = ''

    modifiers: [ItemModifier] = []
    corrupted: bool = False

    # TODO: handle influence types, as an enum?
    influence: str = ''

    def __attrs_post_init__(self):
        sockets = self.raw_sockets.lower()
        self.r_sockets = sockets.count('r')
        self.b_sockets = sockets.count('b')
        self.g_sockets = sockets.count('g')
        self.w_sockets = sockets.count('w')
        # TODO: fix link count
        self.links = sockets.count('-')

    def get_pseudo_mods(self):
        raise NotImplementedError

    def get_json(self):
        raise NotImplementedError
