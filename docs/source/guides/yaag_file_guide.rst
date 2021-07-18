================
YAAG Files Guide
================

.. toctree::

   yaag_file_guide


Introduction
************

As YAAG and it's sequels are pretty complicated games (with thousands of
``prints()``), it makes sense to simplify that. Cutewarriorlover, the Reform
lead developer, has developed a system that parses a ``.yaag`` file and returns
a Python ``list`` of resulting elements. While this is simpler than before, it
might still get confusing. This guide documents everything that is in the
``.yaag`` files, with a goal to let anyone with contributing intentions to
understand and use YAAG files.


How It Works
************

.. Note::
    If you're just looking for documentation about the YAAG files, I recommend
    you skip this part. This is only for people who would like to understand
    the internals of this system.

As any programming language, YAAG files use a lexer. However, since YAAG files
are... peculiar in a sort of way, it is impossible to parse it using a normal
lexer. The current lexer takes a line, and uses it's indentation to try to
figure out which type it is.

Parameters
----------

Because any line that starts with a 4-space indent is considered a parameter
line, any line that is indented is not tokenized, instead giving a ``Token()``
with a type of ``parameter``.

Commands
--------

However, the commands are different. While most programming languages (like
Python) give ``SyntaxError``'s at the parsing stage, YAAG files check for
syntax at the tokenization stage (because they don't really *have* a parsing
stage). If a line that doesn't have indentation (and isn't an empty line) that
doesn't start with a ``[`` is encountered, an error is raised. Otherwise, the
command is tokenized, and depending on whether it encounters a special
parameter, also tokenizes that too. Then, when a token is finished generating,
it compares said token with a table to check if the number of parameters,
special parameters, and special parameter type is correct.


Syntax
******

The syntax of YAAG files look pretty simple. Here's an example:

.. code-block:: text

    [dialogue advance]
        Hello!
        I'm in some dialogue!
        Gee, how exciting...
        Hey! Don't insult YAAG files!

The intent of this piece of code should look obvious. Here's an explanation.

Commands
--------

Simply put, a command is something the program should do. In the example above,
``[dialogue]`` is the command. Yes, you might be shouting at me that I missed
an ``advance`` part. That's because that's not part of the command. Now
introducing...

Command Special Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^

A command can have something called a ``special parameter``, which is basically
that. A special parameter. Each command can have at most one, and sometimes
those are optional. They go after the command, and in the previous example, the
``advance`` would be the special parameter (for what it does, refer to the
documentation on the ``[dialogue]`` command).

Command Parameters
^^^^^^^^^^^^^^^^^^

A command can have a list of parameters that act as extra information to said
command. Commands can have parameters that have an unlimited number of values
(for an example, check out the ``[dialogue]`` command). If written correctly,
a parameter can be parsed as a number, but they are usually strings.


Commands
********

This is a list of commands that are currently in YAAG files.

``[dialogue]``
--------------

This is usually the most common command. It just prints out a list of strings.

Parameters
^^^^^^^^^^

.. glossary::
    ``args*`` - String
        A list of messages to print out.

Special Parameters
^^^^^^^^^^^^^^^^^^

.. glossary::
    ``advance`` - Boolean
        The ``advance`` special parameter is a boolean, indicating whether to use the ``input()`` function after each print.


``[decision]``
--------------

A decision is a question presented to the user, with a list of possible choices.
The user is them prompted to answer the question using numbers, representing the choices.

Parameters
^^^^^^^^^^

.. glossary::
    ``args*`` - String
        A list of possible choices to present to the user

Special Parameters
^^^^^^^^^^^^^^^^^^

.. glossary::
    ``question`` - String
        The question to present to the user

``[quiz]``
----------

A question is presented to the user, who then is prompted to answer freely. If
the user's answer is one of the possible answers, then give the user predefined
stat boosts.

Parameters
^^^^^^^^^^

.. glossary::
    ``answer`` - String
        The answer to the question

        .. Note::
            This answer is case-insensitive. If the answer is ``abc`` and the
            user answers ``aBc``, it still counts.

    ``stat_boost`` - String
        The stat boost to give to the player if the answer is correct, represented in a Python runnable string


``[run]``
---------

The run command is self-explanatory: it runs a ``.yaag`` file!

Special Parameters
^^^^^^^^^^^^^^^^^^

.. glossary::
    ``file`` - String
        The ``.yaag`` file to run.

Parameters
^^^^^^^^^^

.. Attention::
    There are no parameters for the ``[run]`` command.


``[room]``
----------

The room command is partly self-explanatory: it changes the current player's
room. This command should be at the start of every file, so when you run a
file, the room changes.

Special Parameters
^^^^^^^^^^^^^^^^^^

.. glossary::
    ``room_name`` - String
        The name of the room to change to.

Parameters
^^^^^^^^^^

.. Attention::
    There are no parameters for the ``[room]`` command.


``[fight]``
-----------

The fight command initiates a fight between the player and another mob. Said
mob's stats should be documented in another file ``mobs.json``.

Special Parameters
^^^^^^^^^^^^^^^^^^

.. glossary::
    ``mob_name``
        The name of the mob, which maps to a list of stats inside the aforementioned ``mobs.json`` file.

Parameters
^^^^^^^^^^

.. Attention::
    There are no parameters for the ``[fight]`` command.
