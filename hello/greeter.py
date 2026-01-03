class Greeter:
    """Responsible for generating greeting messages."""

    def __init__(self, name: str = "World"):
        self.name = name

    def greet(self) -> str:
        return f"Hello {self.name}!"
