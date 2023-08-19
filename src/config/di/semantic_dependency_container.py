from dependency_injector import containers, providers

from src.semantic.domain.repository.semantic_repository import SemanticRepository
from src.semantic.infrastructure.semantic_extract_model_impl import SemanticExtractModelImpl


class SemanticDependencyContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.semantic.application.query.create_semantic_query",
            "src.semantic.application.query.delete_semantic_query",
            "src.semantic.application.query.read_semantic_query",
            "src.semantic.application.service.update_semantic_service"
        ]
    )

    semantic_extract_model = providers.Singleton(SemanticExtractModelImpl)
    semantic_repository = providers.Singleton(SemanticRepository)
