from typing import Protocol

from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.music.domain.model.lyrics_vo import LyricsVO
from src.music.domain.repository.semantic_dto import SemanticDto


class SemanticQuery(Protocol):

    def create_semantic(self, lyrics: LyricsVO) -> SemanticIdVO:
        pass

    def get_semantic_by_id(self, semantic_id: SemanticIdVO) -> SemanticDto:
        pass
