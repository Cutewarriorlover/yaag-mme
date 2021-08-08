from yaag_mme.yaag_parser import parse_file, YaagTransformer


def execute(filename, game):
    parsed = parse_file(filename)
    transformed = YaagTransformer().transform(parsed)

    for command in transformed.children:
        command.execute(game)
