
class Title(str):
    def __new__(cls, value: str = None):
        if not value:
            raise ValueError("Title cannot be empty")
        value = value.strip()
        if len(value) > 200:
            raise ValueError("Title too long")
        return super().__new__(cls, value)
