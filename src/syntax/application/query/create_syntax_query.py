from dependency_injector.wiring import inject, Provide

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.config.di.syntax_dependency_container import SyntaxDependencyContainer
from src.syntax.domain.model.feature_vo import FeatureVO
from src.syntax.domain.model.syntax import Syntax
from src.syntax.domain.repository.syntax_api import SyntaxApi
from src.syntax.domain.repository.syntax_repository import SyntaxRepository


class CreateSyntaxQuery:

    __syntax_api: SyntaxApi
    __syntax_repository: SyntaxRepository

    @inject
    def __init__(
            self,
            syntax_api: SyntaxApi = Provide[SyntaxDependencyContainer.syntax_api],
            syntax_repository: SyntaxRepository = Provide[SyntaxDependencyContainer.syntax_repository]
    ):
        self.__syntax_api = syntax_api
        self.__syntax_repository = syntax_repository

    def create_and_save_syntax_by_music_id(self, music_id: MusicIdVO):
        new_syntax_id: SyntaxIdVO = SyntaxIdVO(music_id.id)
        new_feature: FeatureVO = self.__syntax_api.get_feature_by_music_id(music_id)
        new_syntax: Syntax = Syntax(
            syntax_id=new_syntax_id,
            music_id=music_id,
            feature=new_feature
        )
        self.__syntax_repository.save_syntax(new_syntax)
        return new_syntax
