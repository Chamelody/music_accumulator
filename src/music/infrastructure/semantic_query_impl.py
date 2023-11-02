from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.music.domain.model.lyrics_vo import LyricsVO
from src.music.domain.repository.semantic_dto import SemanticDto
from src.music.domain.repository.semantic_query import SemanticQuery


class SemanticQueryImpl(SemanticQuery):

    def create_semantic(self, music_id: MusicIdVO, lyrics: LyricsVO) -> SemanticIdVO:
        pass

    def delete_semantic_by_id(self, semantic_id: SemanticIdVO) -> bool:
        pass

    def get_semantic_by_id(self, semantic_id: SemanticIdVO) -> SemanticDto:
        pass
