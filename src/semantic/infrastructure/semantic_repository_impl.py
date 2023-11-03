from typing import Optional

from sqlalchemy.exc import SQLAlchemyError

from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.config.database.sqlalchemy_config import session
from src.semantic.domain.model.semantic import Semantic
from src.semantic.domain.repository.semantic_repository import SemanticRepository
from src.semantic.infrastructure.mapper.semantic_object_mapper import SemanticObjectMapper
from src.semantic.infrastructure.model.semantic_do import SemanticDO


class SemanticRepositoryImpl(SemanticRepository):

    def get_semantic_by_id(self, semantic_id: SemanticIdVO) -> Optional[Semantic]:
        try:
            semantic_do: SemanticDO = session.query(SemanticDO)\
                                             .filter(SemanticDO.semantic_id == semantic_id.id)\
                                             .first()
            if semantic_do is None:
                return None
            return SemanticObjectMapper.semantic_do_to_entity(semantic_do)
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            return None

    def get_all_semantics(self) -> list[Semantic]:
        try:
            all_semantic_do: list[SemanticDO] = session.query(SemanticDO).all()
            return list(map(SemanticObjectMapper.semantic_do_to_entity, all_semantic_do))
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            return []

    def save_semantic(self, semantic: Semantic) -> bool:
        semantic_do: SemanticDO = SemanticObjectMapper.semantic_entity_to_do(semantic)
        try:
            session.add(semantic_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False

    def update_semantic(self, semantic: Semantic) -> bool:
        try:
            semantic_do: SemanticDO = session.query(SemanticDO)\
                                             .filter(SemanticDO.semantic_id == semantic.semantic_id.id)\
                                             .first()
            session.add(semantic_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False

    def delete_semantic_by_id(self, semantic_id: SemanticIdVO) -> bool:
        try:
            semantic_do: SemanticDO = session.query(SemanticDO)\
                                             .filter(SemanticDO.semantic_id == semantic_id.id)\
                                             .first()
            session.delete(semantic_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False
