from typing import Optional

from dependency_injector.wiring import inject, Provide

from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.config.di.semantic_infra_dependency_container import SemanticInfraDependencyContainer
from src.semantic.domain.model.semantic import Semantic
from src.semantic.domain.repository.semantic_repository import SemanticRepository


class ReadSemanticQuery:

    __semantic_repository: SemanticRepository

    @inject
    def __init__(
            self,
            semantic_repository: SemanticRepository = Provide[SemanticInfraDependencyContainer.semantic_repository]
    ):
        self.__semantic_repository = semantic_repository

    def get_semantic_by_id(self, semantic_id: SemanticIdVO) -> Optional[Semantic]:
        return self.__semantic_repository.get_semantic_by_id(semantic_id)

    def get_all_semantics(self) -> list[Semantic]:
        return self.__semantic_repository.get_all_semantics()
