import os.path

import pytest
import pathlib

from yaag_mme.player import Player
from yaag_mme.yaag_parser import parser, execute

path = pathlib.Path(os.path.abspath("./yaag_mme/story"))


class TestYaagParser:
    @pytest.mark.parametrize("file", path.glob("**/*.yaag"),
                             ids=[i.name for i in path.glob("**/*.yaag")])
    def test_parser(self, file):
        print(parser.parse(file.read_text()))

    def test_executor(self):
        class MockGame:
            def __init__(self):
                self.state = {
                    "hero_name": "mock_hero",
                    "epilogue_id": 0
                }
                self.player = Player("mock_player")

        print(execute("./yaag_mme/story/epilogue/id0.yaag", MockGame()))
