from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.syntax.domain.repository.syntax_repository import SyntaxRepository


class DeleteSyntaxQuery:

    __syntax_repository: SyntaxRepository

    def __init__(self, syntax_repository: SyntaxRepository):
        self.__syntax_repository = syntax_repository

    def delete_syntax_by_id(self, syntax_id: SyntaxIdVO) -> bool:
        return self.__syntax_repository.delete_syntax_by_id(syntax_id)
