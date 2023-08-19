from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.semantic.domain.model.semantic import Semantic
from src.semantic.domain.repository.semantic_repository import SemanticRepository


class ReadSemanticService:

    __semantic_repository: SemanticRepository

    def __init__(self, semantic_repository: SemanticRepository):
        self.__semantic_repository = semantic_repository

    def get_semantic_by_id(self, semantic_id: SemanticIdVO) -> Semantic:
        return self.__semantic_repository.get_semantic_by_id(semantic_id)

    def get_all_semantics(self) -> list[Semantic]:
        return self.__semantic_repository.get_all_semantics()
