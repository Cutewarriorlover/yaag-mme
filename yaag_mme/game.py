import json

from collections import deque

from src.armor import ChainArmor
from src.enums import GameScreen, GameRoom
from src.errors import PlayerNotInitializedError
from src.player import get_player
from src.printer import Printer
from src.utils import is_blank
from src.weapons import StoneSword
from src.yaag_parser import parse_file


class Game:
    def __init__(self):
        self.state = {
            "screen": GameScreen.TITLE,
            "playing": True,
            "room": GameRoom.START,
            "heroName": "",
            "epilogueId": 0
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
        """The game's title screen, which decides your player name and introduces the advance mechanic."""
        print(
            "To play this game, you must type your answers. Also, to advance the story, press enter."
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
            self.execute_yaag_file("states/epilogue/id0.yaag")
        self.state["playing"] = False

    def epilogue(self):
        """The game's epilogue."""

    def execute_yaag_file(self, filename):
        """
        Execute a ``.yaag`` file

        Args:
            filename (str): The file to execute.
        """
        if self.player is None:
            raise PlayerNotInitializedError(
                "To parse and execute a YAAG file, "
                "the player must be initialized.")

        parsed = parse_file(filename, self)
        print("\n\n\n")
        for item in parsed:
            if item["type"] == "dialogue":
                map(self.printer.print, item["messages"])
            elif item["type"] == "dialogue_advance":
                deque(
                    self.printer.print(message, advance=True)
                    for message in item["messages"])
            elif item["type"] == "decision":
                print(item["question"])

                for index, option in enumerate(item["options"]):
                    print(f"{index + 1} - {option}")

                print()
                choice = None
                while choice is None:
                    choice = input("Decision: ")
                    if is_blank(choice):
                        print("Please give a valid number!")
                        choice = None
                    elif not choice.isnumeric():
                        print("Please choose a number!")
                        choice = None
                    elif not 0 < int(choice) <= len(item["options"]):
                        print("Please choose an option between 1 and "
                              f"{len(item['options'])} (inclusive)!")
                        choice = None
                    else:
                        choice = int(choice)
                self.execute_yaag_file(item["files"][choice])
