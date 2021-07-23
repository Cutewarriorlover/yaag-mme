class Parameter:
    def __init__(self, value, file=None):
        self.value = value
        self.file = file

    def __repr__(self):
        return f"""
    {self.value} {"" if self.file is None else "[" + self.file + "]"}
""".strip()
