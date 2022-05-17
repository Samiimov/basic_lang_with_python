class Token:
    def __init__(self, type_, value) -> None:
        self.type = type_
        self.value = value

    def __repr__(self) -> str:
        return  f"Token( Type: {self.type}, Value : {self.value} )"