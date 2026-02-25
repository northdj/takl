
class Description(str):
    def __new__(cls, value: str = None):
        if value:
            value = value.strip()
        
            if len(value) > 300:
                raise ValueError("Description too long")
        return super().__new__(cls, value)
