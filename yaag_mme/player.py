from src.armor import Armor
from src.enums import GameScreen
from src.errors import PlayerAlreadyHasItemError
from src.utils import is_blank, lower_equals, lower_in
from src.weapons import Weapon


def get_player(game, codes):
    """
    Returns a player from a list of inputs by the actual player.

    From the input of a user, this function gives the player's ``Player``
    instance with the name. This also sets the game's ``alphaName``, which
    is the name of the player in YAAG Alpha (defaults to ``WarriorGold001``).
    This function directly modifies ``game``'s ``heroName``.

    Args:
      game(Game): The main ``Game`` object
      codes(List[dict]): A list of character codes that can be used to represent a special player username.

    Returns:
        Player: A new ``Player`` instance based on the user's input.
    """
    def get_hero_name():
        while not game.state["heroName"]:
            print("Have you played Yet Another Adventure Game?")
            hero_decider = input("Yes or No? ")
            if lower_equals(hero_decider, "yes"):
                hero_name_to_be = input("What was your name in that game? ")
                if is_blank(hero_name_to_be):
                    print(
                        "Your name could not be blank. Please enter a different name.\n"
                    )
                else:
                    print("Thank you.")
                    input()
                    game.state["heroName"] = hero_name_to_be
            elif lower_equals(hero_decider, "no"):
                print("Thank you.")
                input()
                game.state["heroName"] = "WarriorGold001"
            else:
                print("Please select a valid option.")

    def test_character_code():
        input_code = input("What is your code? ")
        for code, username in codes.items():
            if input_code == code:
                print(f"Welcome, {username}")
                info.update({"name": username})
                game.state["screen"] = GameScreen.GAME
                break
        if not info.get("name"):
            print("That's not a valid code.")
            print("")

    def get_name():
        taken_names = ("eevee005", "murdlemuffin", "tear 2bad",
                       game.state["heroName"])

        player_name = input("What is your name? ")
        if player_name.lower() == "dino-pack":
            print("Hey! That's me. You can't take that name.\n")
            print("Try again.\n")
        elif lower_in(player_name, taken_names):
            print("That name is taken, please try again.\n")
        elif is_blank(player_name):
            print("Your name cannot be blank. Please try again.\n")
        else:
            info.update({"name": player_name})
            game.state["screen"] = GameScreen.GAME

    info = {}

    get_hero_name()

    while not info.get("name"):
        print("Do you have a character code?")
        character_code = input("Yes or No? ")
        if character_code.lower() == "yes":
            test_character_code()
        elif character_code.lower() == "no":
            get_name()

    return Player(info["name"])


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.equipped = {"sword": None, "armor": None}
        self.stats = {
            "charisma": 0,
            "luck": 0,
            "health": 10,
            "maxHealth": 10,
            "healing": 4,
            "power": 1,
            "defense": 1,
        }

    def heal(self):
        r"""
        Heals the player for an amount of health.

        This function heals the player directly. Anything outside the
        ``Player`` class should not directly use ``player.stats["health"]``,
        instead using the ``heal()`` and ``damage()`` methods. The amount
        of health healed is the amount of ``healing`` stat the player has.
        This function has no calculations; the ``healing`` stat *is* the
        amount of health healed.
        """
        if self.stats["healing"] + self.stats["health"] > self.stats[
                "maxHealth"]:
            self.stats["health"] = self.stats["maxHealth"]
        else:
            self.stats["health"] += self.stats["healing"]

    def damage(self, damage):
        r"""
        Deals ``damage`` damage to the player.

        This function heals the player directly. Anything outside the
        ``Player`` class should not directly use ``player.stats["health"]``,
        instead using the ``heal()`` and ``damage()`` methods. Damage dealt
        is calculated with the following equation:

        .. math::
            x = a \times (\frac{b}{b\:+\:50})

        Where ``x`` is the amount of damage the player will receive, ``a`` is
        the damage dealt by the enemy (``x`` is final damage, ``a`` is dealt
        damage), and ``b`` is the player's defense.

        Args:
            damage (int):
                The damage dealt by the enemy, to be calculated
                against the player's defense and calculate
                final damage.
        """
        raise NotImplementedError()

    def print_inventory(self):
        print("Your inventory:")

        print("  Weapons:")
        for item in self.inventory.items:
            if isinstance(item, Weapon):
                print(
                    f"    {item.name} x{self.inventory.items.count(item)}" +
                    (" (Equipped)" if item is self.equipped["sword"] else ""))

        print("\n  Armor:")
        for item in self.inventory.items:
            if isinstance(item, Armor):
                print(
                    f"    {item.name} x{self.inventory.items.count(item)}" +
                    (" (Equipped)" if item is self.equipped["armor"] else ""))

        print("\n  Other:")
        for item in self.inventory.items:
            if not isinstance(item, Weapon) and not isinstance(item, Armor):
                print(f"    {item.name} x{self.inventory.items.count(item)}")


class Inventory:
    def __init__(self):
        self.items = []
        self.weapons = []
        self.armor = []
        self.other = []

    def add(self, item):
        if any(isinstance(x, type(item))
               for x in self.items) and (issubclass(type(item), Armor)
                                         or issubclass(type(item), Weapon)):
            raise PlayerAlreadyHasItemError("The player already has a(n) " +
                                            item.name)

        self.items.append(item)

        if isinstance(item, Armor):
            self.armor.append(item)
        elif isinstance(item, Weapon):
            self.weapons.append(item)
        else:
            self.other.append(item)
