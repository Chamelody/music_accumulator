from dependency_injector import containers, providers

from src.semantic.application.query.create_semantic_query import CreateSemanticQuery
from src.semantic.application.query.delete_semantic_query import DeleteSemanticQuery
from src.semantic.application.query.read_semantic_query import ReadSemanticQuery
from src.semantic.application.service.update_semantic_service import UpdateSemanticService


class SemanticAppDependencyContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.music.infrastructure.semantic_query_impl"

        ]
    )

    create_semantic_query = providers.Singleton(CreateSemanticQuery)
    read_semantic_query = providers.Singleton(ReadSemanticQuery)
    delete_semantic_query = providers.Singleton(DeleteSemanticQuery)
    update_semantic_service = providers.Singleton(UpdateSemanticService)
