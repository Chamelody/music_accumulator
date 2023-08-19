from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.semantic.domain.repository.semantic_repository import SemanticRepository


class DeleteSemanticService:

    __semantic_repository: SemanticRepository

    def __init__(self, semantic_repository: SemanticRepository):
        self.__semantic_repository = semantic_repository

    def delete_semantic_by_id(self, semantic_id: SemanticIdVO) -> bool:
        return self.__semantic_repository.delete_semantic_by_id(semantic_id)
