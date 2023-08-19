from typing import Protocol

from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.syntax.domain.model.syntax import Syntax


class SyntaxRepository(Protocol):

    def get_syntax_by_id(self, syntax_id: SyntaxIdVO) -> Syntax:
        pass

    def get_all_syntax(self) -> list[Syntax]:
        pass

    def save_syntax(self, syntax: Syntax) -> bool:
        pass

    def update_syntax(self, syntax: Syntax) -> bool:
        pass

    def delete_syntax_by_id(self, syntax_id: SyntaxIdVO) -> bool:
        pass
