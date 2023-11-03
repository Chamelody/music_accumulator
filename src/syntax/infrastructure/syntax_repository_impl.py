from typing import Optional

from sqlalchemy.exc import SQLAlchemyError

from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.config.database.sqlalchemy_config import session
from src.syntax.domain.model.syntax import Syntax
from src.syntax.domain.repository.syntax_repository import SyntaxRepository
from src.syntax.infrastructure.mapper.syntax_object_mapper import SyntaxObjectMapper
from src.syntax.infrastructure.model.syntax_do import SyntaxDO


class SyntaxRepositoryImpl(SyntaxRepository):

    def get_syntax_by_id(self, syntax_id: SyntaxIdVO) -> Optional[Syntax]:
        try:
            syntax_do: SyntaxDO = session.query(SyntaxDO).filter(SyntaxDO.syntax_id == syntax_id.id).first()
            if syntax_do is None:
                return None
            return SyntaxObjectMapper.syntax_do_to_entity(syntax_do)
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            return None

    def get_all_syntax(self) -> list[Syntax]:
        try:
            all_syntax_do: list[SyntaxDO] = session.query(SyntaxDO).all()
            return list(map(SyntaxObjectMapper.syntax_do_to_entity, all_syntax_do))
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            return []

    def save_syntax(self, syntax: Syntax) -> bool:
        syntax_do: SyntaxDO = SyntaxObjectMapper.syntax_entity_to_do(syntax)
        try:
            session.add(syntax_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False

    def update_syntax(self, syntax: Syntax) -> bool:
        try:
            syntax_do: SyntaxDO = session.query(SyntaxDO).filter(SyntaxDO.syntax_id == syntax.syntax_id.id).first()
            session.add(syntax_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False

    def delete_syntax_by_id(self, syntax_id: SyntaxIdVO) -> bool:
        try:
            syntax_do: SyntaxDO = session.query(SyntaxDO).filter(SyntaxDO.syntax_id == syntax_id.id).first()
            session.delete(syntax_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False
