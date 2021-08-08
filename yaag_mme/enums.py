from enum import Enum


class NpcState(Enum):
    """
    An enumeration of all the NPC states (currently ``ALIVE``, ``SPARED``, and ``KILLED``).

    .. Attention:: Everything should be referenced with ``NpcState.STATE_NAME``, without a new
        instance.
    """

    ALIVE = "npc_alive"
    SPARED = "npc_spared"
    KILLED = "npc_killed"


class GameScreen(Enum):
    """
    An enumeration of all the screens (currently ``GAME``, ``TITLE``, and ``EPILOGUE``).

    .. Attention:: Everything should be referenced with ``GameScreen.SCREEN_NAME``, without a new
        instance.
    """

    GAME = "screen_game"
    TITLE = "screen_title"
    EPILOGUE = "screen_epilogue"


class GameRoom(Enum):
    """
    An enumeration of all the rooms.

    .. Attention:: Everything should be referenced with ``GameRoom.ROOM_NAME``, without a new
        instance.
    """

    START = "room_start"
    DINO_KILL_ROOM = "room_dino_kill"
    MURDLE_KILL_ROOM = "room_murdle_kill"
