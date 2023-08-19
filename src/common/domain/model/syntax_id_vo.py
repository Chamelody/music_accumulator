from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO


class SyntaxIdVO:
    __id: str

    def __init__(self, new_id: str):
        self.__id = new_id

    def to_music_id(self) -> MusicIdVO:
        return MusicIdVO(self.id)

    def to_semantic_id(self) -> SemanticIdVO:
        return SemanticIdVO(self.id)

    @property
    def id(self):
        return self.__id
