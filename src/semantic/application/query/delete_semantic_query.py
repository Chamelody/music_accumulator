from dependency_injector.wiring import inject, Provide

from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.config.di.semantic_infra_dependency_container import SemanticInfraDependencyContainer
from src.semantic.domain.repository.semantic_repository import SemanticRepository


class DeleteSemanticQuery:

    __semantic_repository: SemanticRepository

    @inject
    def __init__(
            self,
            semantic_repository: SemanticRepository = Provide[SemanticInfraDependencyContainer.semantic_repository]
    ):
        self.__semantic_repository = semantic_repository

    def delete_semantic_by_id(self, semantic_id: SemanticIdVO) -> bool:
        return self.__semantic_repository.delete_semantic_by_id(semantic_id)
