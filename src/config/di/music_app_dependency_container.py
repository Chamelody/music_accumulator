from dependency_injector import containers, providers

from src.music.application.create_music_service import CreateMusicService
from src.music.application.delete_music_service import DeleteMusicService
from src.music.application.read_music_service import ReadMusicService
from src.music.application.update_music_service import UpdateMusicService


class MusicAppDependencyContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.music.presentation.music_controller",
            "src.music.presentation.music_popularity_update_scheduler"
        ]
    )

    create_music_service = providers.Singleton(CreateMusicService)
    read_music_service = providers.Singleton(ReadMusicService)
    update_music_service = providers.Singleton(UpdateMusicService)
    delete_music_service = providers.Singleton(DeleteMusicService)
