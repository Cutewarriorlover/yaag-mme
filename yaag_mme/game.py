import json

from yaag_mme.armor import ChainArmor
from yaag_mme.enums import GameScreen, GameRoom
from yaag_mme.player import get_player, Player
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
        self.debug = False

    def play(self, debug):
        """Start the game!"""
        self.debug = debug
        while self.state["playing"]:
            if self.state["screen"] == GameScreen.TITLE:
                self.title_screen()
            elif self.state["screen"] == GameScreen.GAME:
                self.game_screen()
            elif self.state["screen"] == GameScreen.EPILOGUE:
                self.epilogue_screen()

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

        if not self.debug:
            with open("config.json") as file:
                info = get_player(self, json.load(file)["codes"])
                self.player = Player(info.name)
                self.state["hero_name"] = info["hero_name"]
        else:
            self.player = Player("DebugPlayer")
            self.state["hero_name"] = "DebugHero"

        # Starting items
        self.player.inventory.add(StoneSword())
        self.player.inventory.add(ChainArmor())

        self.state["room"] = GameRoom.START
        self.state["screen"] = GameScreen.GAME

    def game_screen(self):
        """The game's main gameplay."""
        if self.state["room"] == GameRoom.START:
            execute("story/intro/start.yaag", self)
        self.state["playing"] = False

    def epilogue_screen(self):
        """The game's epilogue."""
