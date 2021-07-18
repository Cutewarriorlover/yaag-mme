from yaag_mme.yaag_parser.lexer import Lexer


class TestYaagParser:
    def setup_method(self):
        self.yaag_file = r"""
[dialogue advance]

    One week later...

    You spawn in the dungeon, where four other players were already waiting. On one wall, was a big sign, listing all the players' names.{{\n\n}}You read the sign. It says:{{\n\n}}"Tear 2bad, MurdleMuffin, Dino-Pack, and {{player_name}}."

    "So those are the people I'm teaming with, huh?" you think.

    You feel a tap on your shoulder. You turn around.

    "Hi! My name is Dino-Pack. I'm just going around, introducing myself to everyone. Now that you're here, the entire party has arrived. I'm exited to start the dungeon!" says the man who tapped your shoulder.

    You take a good look at Dino-Pack. He has short, brown hair, with a matching eye colour. He's wearing a white hoodie, and brown khaki pants. He's wearing glasses, which are slightly dirty.

    "So, what's your name?" asks Dino-Pack.

    "Oh! My name is {{player_name}}" you answer.

    "Nice to meet you, {{player_name}}! Come on, let's go meet the others," replies Dino-Pack, walking towards a woman who is leaning against a wall.{{\n\n}}You walk up to her, while she's reading something on a peice of paper.

    "Hello?" says Dino-Pack to the woman, getting her attention. She looks up.{{\n\n}}"Oh, hi! Nice to meet you two! My name is Eevee005. What about you?" she asks with a smile.{{\n\n}}"My name is Dino-Pack, nice to meet you too!" says Dino-Pack, slightly flustered.{{\n\n}}"My name is {{player_name}}," you reply simply.

    "She's quite charming," you think. She has brown hair, like Dino-Pack, but unlike him, her hair goes down about one quarter of her back. She has blue eyes, and is wearing a green hoodie. Her hoodie has a cartoon heart on it. She's slightly shorter than Dino-Pack.

    "Have you two noticed how complicated this game is? I'm reading this player guide, and it talks about so many mechanics..." says Eevee005, holding up her paper.{{\n\n}}"No, I haven't read anything about this game yet. I wanted to meet everyone first," replies Dino-Pack. "Speaking of... We should go meet the other two," suggests Dino-Pack.

    "Good idea," agrees Eevee005. She looks across the room, where the other two players are. "But who do we speak to first?" asks Eevee005.{{\n\n}}"How about {{player_name}} decides?" proposes Dino-Pack. Eevee005 nods.

    ---Decision Time---{{\n\n}}This game will feature decisions. Some of them may change the course of the game, and others will not. This one acts as a tutorial.

[decision "Who will you speak to first?"]
    The guy sitting in one corner. [choices/murdle.yaag]
    The guy getting ready for the dungeon run in another corner. [choices/tear.yaag]
        """.strip()

    def test_tokenize(self):
        assert Lexer.tokenize(self.yaag_file) == "[(TOKEN TokenType.COMMAND [dialogue advance]), (TOKEN TokenType.PARAMETER     One week later...), (TOKEN TokenType.PARAMETER     You spawn in the dungeon, where four other players were already waiting. On one wall, was a big sign, listing all the players' names.{{\n\n}}You read the sign. It says:{{\n\n}}\"Tear 2bad, MurdleMuffin, Dino-Pack, and {{player_name}}.\"), (TOKEN TokenType.PARAMETER     \"So those are the people I'm teaming with, huh?\" you think.), (TOKEN TokenType.PARAMETER     You feel a tap on your shoulder. You turn around.), (TOKEN TokenType.PARAMETER     \"Hi! My name is Dino-Pack. I'm just going around, introducing myself to everyone. Now that you're here, the entire party has arrived. I'm exited to start the dungeon!\" says the man who tapped your shoulder.), (TOKEN TokenType.PARAMETER     You take a good look at Dino-Pack. He has short, brown hair, with a matching eye colour. He's wearing a white hoodie, and brown khaki pants. He's wearing glasses, which are slightly dirty.), (TOKEN TokenType.PARAMETER     \"So, what's your name?\" asks Dino-Pack.), (TOKEN TokenType.PARAMETER     \"Oh! My name is {{player_name}}\" you answer.), (TOKEN TokenType.PARAMETER     \"Nice to meet you, {{player_name}}! Come on, let's go meet the others,\" replies Dino-Pack, walking towards a woman who is leaning against a wall.{{\n\n}}You walk up to her, while she's reading something on a peice of paper.), (TOKEN TokenType.PARAMETER     \"Hello?\" says Dino-Pack to the woman, getting her attention. She looks up.{{\n\n}}\"Oh, hi! Nice to meet you two! My name is Eevee005. What about you?\" she asks with a smile.{{\n\n}}\"My name is Dino-Pack, nice to meet you too!\" says Dino-Pack, slightly flustered.{{\n\n}}\"My name is {{player_name}},\" you reply simply.), (TOKEN TokenType.PARAMETER     \"She's quite charming,\" you think. She has brown hair, like Dino-Pack, but unlike him, her hair goes down about one quarter of her back. She has blue eyes, and is wearing a green hoodie. Her hoodie has a cartoon heart on it. She's slightly shorter than Dino-Pack.), (TOKEN TokenType.PARAMETER     \"Have you two noticed how complicated this game is? I'm reading this player guide, and it talks about so many mechanics...\" says Eevee005, holding up her paper.{{\n\n}}\"No, I haven't read anything about this game yet. I wanted to meet everyone first,\" replies Dino-Pack. \"Speaking of... We should go meet the other two,\" suggests Dino-Pack.), (TOKEN TokenType.PARAMETER     \"Good idea,\" agrees Eevee005. She looks across the room, where the other two players are. \"But who do we speak to first?\" asks Eevee005.{{\n\n}}\"How about {{player_name}} decides?\" proposes Dino-Pack. Eevee005 nods.), (TOKEN TokenType.PARAMETER     ---Decision Time---{{\n\n}}This game will feature decisions. Some of them may change the course of the game, and others will not. This one acts as a tutorial.), (TOKEN TokenType.COMMAND [decision \"Who will you speak to first?\"]), (TOKEN TokenType.PARAMETER     The guy sitting in one corner. [choices/murdle.yaag]), (TOKEN TokenType.PARAMETER     The guy getting ready for the dungeon run in another corner. [choices/tear.yaag])]"
