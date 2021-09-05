"""Console script for yaag_mme."""
import os
import sys
import click

from yaag_mme.game import Game


@click.command()
@click.option("--debug", "-d", is_flag=True, help="Run game in Debug mode")
def main(debug):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    game = Game()
    game.play(debug)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
