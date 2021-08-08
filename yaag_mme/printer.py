class Printer:
    """
    A basic printer

    .. Attention:: There should only be one instance of this class at all times.

    Attributes:
        debug (bool):
            Whether this logger / printer is a debugging logger (and, thus, whether this logger should print out it's
            message without a ``-d`` / ``--debug`` flag.)
        name (str):
            The name of this logger. This is only required if ``debug`` is ``True``.
    """

    def __init__(self, *, debug=False, name="debug"):
        self.debug = debug
        self.name = name

    def print(self, message, *, advance=False):
        """
        Print a message to stout. If ``chat`` is ``True``, then print the
        message, video game chat style.

        This function is a wrapper around the ``print()`` function, with a
        ``chat`` flag that indicates whether to print out ``message`` in
        video game chat style. This also has an ``advance`` flag that
        indicates whether to have an ``input()`` function after printing
        out the message.

        Args:
            message (str):
                The message to print.

            chat (bool, optional):
                Whether to print out the message video game chat style,
                defaults to False.

            user (str, optional):
                Only required if ``chat`` is ``True``, the user sending the
                message, defaults to "".

            advance (bool, optional):
                Whether to add an ``input()`` after the ``print()``, thus
                advancing the game, defaults to False.
        """
        print(message)

        if advance:
            input()
