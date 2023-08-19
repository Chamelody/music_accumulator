from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO


class MusicIdVO:
    __id: str

    def __init__(self, new_id: str):
        self.__id = new_id

    def to_semantic_id(self) -> SemanticIdVO:
        return SemanticIdVO(self.id)

    def to_syntax_id(self) -> SyntaxIdVO:
        return SyntaxIdVO(self.id)

    @property
    def id(self):
        return self.__id
