"""Console script for yaag_mme."""
import os
import sys
import click

from yaag_mme.game import Game


@click.command()
def main(args=None):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    game = Game()
    game.play()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
