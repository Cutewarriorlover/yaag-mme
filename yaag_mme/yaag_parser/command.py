class Command:
    def __init__(self, command_name, special_parameter=None, parameters=None):
        if not parameters:
            parameters = []

        self.command_name = command_name
        self.special_parameter = special_parameter
        self.parameters = parameters

    def __repr__(self):
        return f"""
[{self.command_name} {self.special_parameter}]
        """.strip()
