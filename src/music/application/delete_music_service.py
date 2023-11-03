from dependency_injector.wiring import inject, Provide

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.config.di.music_infra_dependency_container import MusicInfraDependencyContainer
from src.music.domain.repository.music_repository import MusicRepository
from src.music.domain.repository.semantic_query import SemanticQuery
from src.music.domain.repository.syntax_query import SyntaxQuery


class DeleteMusicService:
    __music_repository: MusicRepository
    __syntax_query: SyntaxQuery
    __semantic_query: SemanticQuery

    @inject
    def __init__(
            self,
            music_repository: MusicRepository = Provide[MusicInfraDependencyContainer.music_repository],
            syntax_query: SyntaxQuery = Provide[MusicInfraDependencyContainer.syntax_query],
            semantic_query: SemanticQuery = Provide[MusicInfraDependencyContainer.semantic_query]
    ):
        self.__music_repository = music_repository
        self.__syntax_query = syntax_query
        self.__semantic_query = semantic_query

    def delete_music_by_id(self, music_id: MusicIdVO) -> bool:
        self.__syntax_query.delete_syntax_by_id(SyntaxIdVO(music_id.id))

        return self.__syntax_query.delete_syntax_by_id(SyntaxIdVO(music_id.id)) and \
            self.__semantic_query.delete_semantic_by_id(SemanticIdVO(music_id.id)) and \
            self.__music_repository.delete_music_by_id(music_id)
