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
documentation on the ``[dialogue]`` command.)
