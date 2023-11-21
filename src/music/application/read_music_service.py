from typing import Optional

from dependency_injector.wiring import inject, Provide

from src.common.domain.model.music_id_vo import MusicIdVO
from src.config.di.music_infra_dependency_container import MusicInfraDependencyContainer
from src.music.domain.model.music import Music
from src.music.domain.repository.music_repository import MusicRepository
from src.music.domain.repository.semantic_dto import SemanticDto
from src.music.domain.repository.semantic_query import SemanticQuery
from src.music.domain.repository.syntax_dto import SyntaxDto
from src.music.domain.repository.syntax_query import SyntaxQuery


music_information_type = tuple[Music, SyntaxDto, SemanticDto]


class ReadMusicService:
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

    def get_music_by_id(self, music_id: MusicIdVO) -> Optional[Music]:
        return self.__music_repository.get_music_by_id(music_id)

    def get_all_music(self) -> list[Music]:
        return self.__music_repository.get_all_music_list()

    def get_music_with_features(self, music_id: MusicIdVO) -> Optional[music_information_type]:
        music: Music = self.get_music_by_id(music_id)
        if music is None:
            return None
        syntax_dto: SyntaxDto = self.__syntax_query.get_syntax_by_id(music.syntax_id)
        semantic_dto: SemanticDto = self.__semantic_query.get_semantic_by_id(music.semantic_id)
        return music, syntax_dto, semantic_dto

    def get_all_music_with_features(self) -> list[music_information_type]:
        all_music_list: list[Music] = self.get_all_music()
        result: list[music_information_type] = list()
        for music in all_music_list:
            syntax_dto: SyntaxDto = self.__syntax_query.get_syntax_by_id(music.syntax_id)
            semantic_dto: SemanticDto = self.__semantic_query.get_semantic_by_id(music.semantic_id)
            result.append((music, syntax_dto, semantic_dto))
        return result
