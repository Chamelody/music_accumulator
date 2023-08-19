from src.syntax.domain.model.feature_vo import FeatureVO
from src.syntax.domain.model.syntax import Syntax
from src.syntax.domain.repository.syntax_api import SyntaxApi
from src.syntax.domain.repository.syntax_repository import SyntaxRepository


class UpdateSyntaxService:

    __syntax_api: SyntaxApi
    __syntax_repository: SyntaxRepository

    def __init__(self, syntax_api: SyntaxApi, syntax_repository: SyntaxRepository):
        self.__syntax_api = syntax_api
        self.__syntax_repository = syntax_repository

    def update_all_feature_by_schedular(self) -> None:
        all_syntax_list: list[Syntax] = self.__syntax_repository.get_all_syntax()
        for syntax in all_syntax_list:
            new_feature: FeatureVO = self.__syntax_api.get_feature_by_music_id(syntax.music_id)
            syntax.update_feature(new_feature)
            self.__syntax_repository.update_syntax(syntax)
