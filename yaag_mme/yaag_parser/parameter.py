class Parameter:
    def __init__(self, value, indent=1):
        self.value = value
        self.indent = indent

    def __repr__(self):
        return f"""{"    " * self.indent}{self.value}"""

    def __str__(self):
        return f"""{self.value}"""
