import os.path

import pytest
import pathlib

from yaag_mme.yaag_parser import parser

path = pathlib.Path(os.path.abspath("./yaag_mme/story"))


class TestYaagParser:
    @pytest.mark.parametrize("file", path.glob("**/*.yaag"), ids=[i.name for i in path.glob("**/*.yaag")])
    def test_parser(self, file):
        print(parser.parse(file.read_text()))
