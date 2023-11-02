from dependency_injector import containers, providers

from src.music.application.create_music_service import CreateMusicService
from src.music.application.delete_music_serivce import DeleteMusicService
from src.music.application.read_music_service import ReadMusicService
from src.music.application.update_music_service import UpdateMusicService
from src.music.infrastructure.music_api_impl import MusicApiImpl
from src.music.infrastructure.music_repository_impl import MusicRepositoryImpl
from src.music.infrastructure.semantic_query_impl import SemanticQueryImpl
from src.music.infrastructure.syntax_query_impl import SyntaxQueryImpl


class MusicDependencyContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.music.application.create_music_service",
            "src.music.application.delete_music_service",
            "src.music.application.read_music_service",
            "src.music.application.update_music_service",
            "src.music.presentation.music_controller",
            "src.music.presentation.music_popularity_update_scheduler"
        ]
    )

    music_api = providers.Singleton(MusicApiImpl)
    music_repository = providers.Singleton(MusicRepositoryImpl)
    syntax_query = providers.Singleton(SyntaxQueryImpl)
    semantic_query = providers.Singleton(SemanticQueryImpl)
    create_music_service = providers.Singleton(CreateMusicService)
    read_music_service = providers.Singleton(ReadMusicService)
    update_music_service = providers.Singleton(UpdateMusicService)
    delete_music_service = providers.Singleton(DeleteMusicService)
