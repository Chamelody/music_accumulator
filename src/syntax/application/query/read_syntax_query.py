from typing import Optional

from dependency_injector.wiring import inject, Provide

from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.config.di.syntax_infra_dependency_container import SyntaxInfraDependencyContainer
from src.syntax.domain.model.syntax import Syntax
from src.syntax.domain.repository.syntax_repository import SyntaxRepository


class ReadSyntaxQuery:

    __syntax_repository: SyntaxRepository

    @inject
    def __init__(
            self,
            syntax_repository: SyntaxRepository = Provide[SyntaxInfraDependencyContainer.syntax_repository]
    ):
        self.__syntax_repository = syntax_repository

    def get_syntax_by_id(self, syntax_id: SyntaxIdVO) -> Optional[Syntax]:
        return self.__syntax_repository.get_syntax_by_id(syntax_id)

    def get_all_syntax_list(self) -> list[Syntax]:
        return self.__syntax_repository.get_all_syntax()
