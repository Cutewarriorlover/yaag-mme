import json

from yaag_mme.armor import ChainArmor
from yaag_mme.enums import GameScreen, GameRoom
from yaag_mme.player import get_player
from yaag_mme.printer import Printer
from yaag_mme.weapons import StoneSword
from yaag_mme.yaag_parser import execute


class Game:
    def __init__(self):
        self.state = {
            "screen": GameScreen.TITLE,
            "playing": True,
            "room": GameRoom.START,
            "hero_name": "",
            "epilogue_id": 0
        }
        self.player = None
        self.printer = Printer()

    def play(self):
        """Start the game!"""
        while self.state["playing"]:
            if self.state["screen"] == GameScreen.TITLE:
                self.title_screen()
            elif self.state["screen"] == GameScreen.GAME:
                self.game()
            elif self.state["screen"] == GameScreen.EPILOGUE:
                self.epilogue()

    def title_screen(self):
        """
            The game's title screen, which decides your player name and
            introduces the advance mechanic.
        """
        print(
            "To play this game, you must type your answers. Also, to advance "
            "the story, press enter."
        )
        print("")
        input("Press enter to begin.")

        with open("config.json") as file:
            self.player = get_player(self, json.load(file)["codes"])

        # Starting items
        self.player.inventory.add(StoneSword())
        self.player.inventory.add(ChainArmor())

    def game(self):
        """The game's main gameplay."""
        if self.state["room"] == GameRoom.START:
            execute("story/intro/start.yaag", self)
        self.state["playing"] = False

    def epilogue(self):
        """The game's epilogue."""
