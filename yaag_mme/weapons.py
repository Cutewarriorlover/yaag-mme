class Weapon:
    def __init__(self):
        self.power = 0
        self.name = "Weapon"
        self.abilities = []


class StoneSword(Weapon):
    def __init__(self):
        super().__init__()
        self.power = 2
        self.name = "Stone Sword"


class SlimyBlade(Weapon):
    def __init__(self):
        super().__init__()
        self.power = 3
        self.name = "Slimy Blade"


class LeadBlade(Weapon):
    def __init__(self):
        super().__init__()
        self.power = 4
        self.name = "Lead Blade"


class GemShortsword(Weapon):
    def __init__(self):
        super().__init__()
        self.power = 5
        self.name = "Gem Shortsword"
