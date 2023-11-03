from dependency_injector import containers, providers

from src.syntax.application.query.create_syntax_query import CreateSyntaxQuery
from src.syntax.application.query.delete_syntax_query import DeleteSyntaxQuery
from src.syntax.application.query.read_syntax_query import ReadSyntaxQuery
from src.syntax.application.service.update_syntax_service import UpdateSyntaxService


class SyntaxAppDependencyContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.music.infrastructure.syntax_query_impl"
        ]
    )

    create_syntax_query = providers.Singleton(CreateSyntaxQuery)
    read_syntax_query = providers.Singleton(ReadSyntaxQuery)
    delete_syntax_query = providers.Singleton(DeleteSyntaxQuery)
    update_syntax_service = providers.Singleton(UpdateSyntaxService)
