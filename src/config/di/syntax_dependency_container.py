from dependency_injector import containers, providers

from src.syntax.infrastructure.syntax_api_impl import SyntaxApiImpl
from src.syntax.infrastructure.syntax_repository_impl import SyntaxRepositoryImpl


class SyntaxDependencyContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.syntax.application.query.create_syntax_query",
            "src.syntax.application.query.delete_syntax_query",
            "src.syntax.application.query.read_syntax_query",
            "src.syntax.application.service.update_syntax_service"
        ]
    )

    syntax_api = providers.Singleton(SyntaxApiImpl)
    syntax_repository = providers.Singleton(SyntaxRepositoryImpl)
