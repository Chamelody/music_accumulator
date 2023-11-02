class SemanticIdVO:
    __id: str

    def __init__(self, new_id: str):
        self.__id = new_id

    @property
    def id(self) -> str:
        return self.__id
