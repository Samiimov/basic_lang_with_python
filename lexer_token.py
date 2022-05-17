class Token:
    def __init__(self, type_, value, name = None) -> None:
        self.type = type_
        self.value = value
        self.name = name

    def __repr__(self) -> str:
        return  f"Token( Type: {self.type}, Value : {self.value}, Name : {self.name})"