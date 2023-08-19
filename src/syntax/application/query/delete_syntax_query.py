from dependency_injector.wiring import inject, Provide

from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.config.di.syntax_dependency_container import SyntaxDependencyContainer
from src.syntax.domain.repository.syntax_repository import SyntaxRepository


class DeleteSyntaxQuery:

    __syntax_repository: SyntaxRepository

    @inject
    def __init__(
            self,
            syntax_repository: SyntaxRepository = Provide[SyntaxDependencyContainer.syntax_repository]
    ):
        self.__syntax_repository = syntax_repository

    def delete_syntax_by_id(self, syntax_id: SyntaxIdVO) -> bool:
        return self.__syntax_repository.delete_syntax_by_id(syntax_id)
