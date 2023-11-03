from dependency_injector.wiring import Provide, inject

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.config.di.syntax_app_dependency_container import SyntaxAppDependencyContainer
from src.music.domain.repository.syntax_dto import SyntaxDto
from src.music.domain.repository.syntax_query import SyntaxQuery
from src.syntax.application.query.create_syntax_query import CreateSyntaxQuery
from src.syntax.application.query.delete_syntax_query import DeleteSyntaxQuery
from src.syntax.application.query.read_syntax_query import ReadSyntaxQuery


class SyntaxQueryImpl(SyntaxQuery):

    __create_syntax_query: CreateSyntaxQuery
    __read_syntax_query: ReadSyntaxQuery
    __delete_syntax_query: DeleteSyntaxQuery

    @inject
    def __init__(
            self,
            create_syntax_query: CreateSyntaxQuery = Provide[SyntaxAppDependencyContainer.create_syntax_query],
            read_syntax_query: ReadSyntaxQuery = Provide[SyntaxAppDependencyContainer.read_syntax_query],
            delete_syntax_query: DeleteSyntaxQuery = Provide[SyntaxAppDependencyContainer.delete_syntax_query]
    ):
        self.__create_syntax_query = create_syntax_query
        self.__read_syntax_query = read_syntax_query
        self.__delete_syntax_query = delete_syntax_query

    def create_syntax_by_music_id(self, music_id: MusicIdVO) -> SyntaxIdVO:
        return self.__create_syntax_query.create_and_save_syntax_by_music_id(music_id=music_id).syntax_id

    def get_syntax_by_id(self, syntax_id: SyntaxIdVO) -> SyntaxDto:
        syntax = self.__read_syntax_query.get_syntax_by_id(syntax_id)
        return SyntaxDto(
            danceability=syntax.feature.danceability,
            energy=syntax.feature.energy,
            music_key=syntax.feature.music_key,
            loudness=syntax.feature.loudness,
            mode=syntax.feature.mode,
            acousticness=syntax.feature.acousticness,
            valence=syntax.feature.valence,
            tempo=syntax.feature.tempo
        )

    def delete_syntax_by_id(self, syntax_id: SyntaxIdVO) -> bool:
        return self.__delete_syntax_query.delete_syntax_by_id(syntax_id)
