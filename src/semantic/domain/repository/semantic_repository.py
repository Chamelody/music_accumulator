from typing import Protocol, Optional

from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.semantic.domain.model.semantic import Semantic


class SemanticRepository(Protocol):

    def get_semantic_by_id(self, semantic_id: SemanticIdVO) -> Optional[Semantic]:
        pass

    def get_all_semantics(self) -> list[Semantic]:
        pass

    def save_semantic(self, semantic: Semantic) -> bool:
        pass

    def update_semantic(self, semantic: Semantic) -> bool:
        pass

    def delete_semantic_by_id(self, semantic_id: SemanticIdVO) -> bool:
        pass
