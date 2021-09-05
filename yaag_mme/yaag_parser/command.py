from yaag_mme.printer import Printer


class Command:
    def __init__(self, type_, special_parameters=None, parameters=None):
        if parameters is None:
            parameters = []
        if special_parameters is None:
            special_parameters = []

        self.type = type_
        self.special_parameters = special_parameters
        self.parameters = parameters

    def __repr__(self):
        return f"""
[{self.type}{" " if self.special_parameters
        else ""}{"".join(self.special_parameters)}]
{chr(10).join([repr(i) for i in self.parameters])}
        """.strip()
