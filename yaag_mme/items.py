class Item:
    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.name = "Item"
        self.description = "This is an item."

    def on_use(self):
        raise NotImplementedError("abstract")

    def __repr__(self):
        return f"{self.name} - {self.description}"


class HealthRestore(Item):
    def __init__(self, player, game):
        super().__init__(player, game)
        self.name = "Health Restore"
        self.description = "Restores your health!"

    def on_use(self):
        self.player.heal()
