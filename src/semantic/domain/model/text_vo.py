class TextVO:
    __text: str

    def __init__(self, text: str):
        self.__text = text

    @property
    def text(self) -> str:
        return self.__text

    def __str__(self) -> str:
        return self.text
