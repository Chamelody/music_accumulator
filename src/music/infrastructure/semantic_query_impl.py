from dependency_injector.wiring import inject, Provide

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.config.di.semantic_app_dependency_container import SemanticAppDependencyContainer
from src.music.domain.model.lyrics_vo import LyricsVO
from src.music.domain.repository.semantic_dto import SemanticDto
from src.music.domain.repository.semantic_query import SemanticQuery
from src.semantic.application.query.create_semantic_query import CreateSemanticQuery
from src.semantic.application.query.delete_semantic_query import DeleteSemanticQuery
from src.semantic.application.query.read_semantic_query import ReadSemanticQuery


class SemanticQueryImpl(SemanticQuery):

    __create_semantic_query: CreateSemanticQuery
    __read_semantic_query: ReadSemanticQuery
    __delete_semantic_query: DeleteSemanticQuery

    @inject
    def __init__(
            self,
            create_semantic_query: CreateSemanticQuery = Provide[SemanticAppDependencyContainer.create_semantic_query],
            read_semantic_query: ReadSemanticQuery = Provide[SemanticAppDependencyContainer.read_semantic_query],
            delete_semantic_query: DeleteSemanticQuery = Provide[SemanticAppDependencyContainer.delete_semantic_query]
    ):
        self.__create_semantic_query = create_semantic_query
        self.__read_semantic_query = read_semantic_query
        self.__delete_semantic_query = delete_semantic_query

    def create_semantic(self, music_id: MusicIdVO, lyrics: LyricsVO) -> SemanticIdVO:
        return self.__create_semantic_query\
            .create_and_save_semantic_by_music_id(music_id=music_id, text=lyrics.lyrics)\
            .semantic_id

    def get_semantic_by_id(self, semantic_id: SemanticIdVO) -> SemanticDto:
        semantic = self.__read_semantic_query.get_semantic_by_id(semantic_id)
        return SemanticDto(
            happy=semantic.emotion.happy,
            sad=semantic.emotion.sad,
            fear=semantic.emotion.fear,
            anger=semantic.emotion.anger,
            love=semantic.emotion.love
        )

    def delete_semantic_by_id(self, semantic_id: SemanticIdVO) -> bool:
        return self.__delete_semantic_query.delete_semantic_by_id(semantic_id)
