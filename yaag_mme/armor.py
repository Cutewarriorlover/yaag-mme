"""
The main entry point for player-wearable armor.

This module gives a main entry point for all armor. Currently, this is all
inside one file, but could be split into more. The class :class:`Armor` is the
main entry point of all armor, being the one to define generic stats.

While all armor classes can have more than one instance in memory at once (to
keep from using the `Singleton Pattern
<https://python-patterns.guide/gang-of-four/singleton/>`_),
it is impossible to add more than one armor piece to any player, as it
will have the appropriate validation, raising an
:exc:`errors.PlayerAlreadyHasItemError`.
"""


class Armor:
    """
    The super-class to any player-wearable armor.

    This class will be extended by any class that desires to be a type of
    player-wearable armor. While there's nothing from keeping the user to do
    so, this class shouldn't be instantiated directly, thus being an abstract
    class.

    Attributes:
        defense(int):
            The amount of defense this piece of armor provides to the player.

            This attribute shouldn't have any use outside of the player class,
            as it only applies to the player's stats (refer to
            :attribute:`player.Player.state` for further information.)
        name(str):
            The name of this piece of armor.

            This name should be a short name (usually under 15 characters that
            is the same as the class's name in title case).

            Some example names are below:

            Good:

            :Iron Armor:
                Adheres to title case. Class should be named ``IronArmor``.
            :Bluefish Armor:
            Adheres to title case. Class should be named ``BluefishArmor``.

            Bad:

            :IronArmor:
                Does not adhere to title case. Should be named ``Iron Armor``
                (extra space) with the *class* named ``IronArmor``.
            :Blue fish Armor:
                Does not adhere to title case. Should be named ``Bluefish
                Armor`` (remove a space) or ``Blue Fish Armor``
                (capitalization) with the class named either ``BluefishArmor``
                 or ``BlueFishArmor`` respectively.
    """
    def __init__(self):
        self.defense = 0
        self.name = "Armor"


class ChainArmor(Armor):
    def __init__(self):
        super().__init__()
        self.defense = 3
        self.name = "Chain Armor"


class RubySuit(Armor):
    def __init__(self):
        super().__init__()
        self.defense = 5
        self.name = "Ruby Suit"
