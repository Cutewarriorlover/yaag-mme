from yaag_mme.yaag_parser import parse_file, YaagTransformer


def replace_parameters(string, game):
    string = string.replace("{{player_name}}", game.player.name)

    return string


def unknown_commmand(command, game):
    print("\n\nUh-Oh! It seems something in this game is not working!")
    print("Please copy the box, and DM it to Cutewarriorlover#6792 on Discord!")
    print("Thanks!\n")

    # TODO: Add box (
    #  ╔═══════════════════════════════════════════════════════════╗
    #  ║                                                           ║
    #  ║                                                           ║
    #  ║                                                           ║
    #  ║                                                           ║
    #  ║                                                           ║
    #  ║                                                           ║
    #  ╚═══════════════════════════════════════════════════════════╝
    #  )
    print(rf"""

""".strip())


def command_dialogue(command, game):
    for message in command.parameters:
        print(replace_parameters(message.value, game))
        if command.special_parameters[0] == "advance":
            input()


commands = {"dialogue": command_dialogue}


def execute(filename, game):
    parsed = parse_file(filename)
    transformed = YaagTransformer().transform(parsed)

    for command in transformed.children:
        commands.get(command.type, unknown_commmand)(command, game)
