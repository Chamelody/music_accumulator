from typing import Optional

from dependency_injector.wiring import inject, Provide

from src.config.di.music_infra_dependency_container import MusicInfraDependencyContainer
from src.music.domain.model.music import Music
from src.music.domain.repository.music_api import MusicApi
from src.music.domain.repository.music_repository import MusicRepository
from src.music.domain.repository.music_request_result import MusicRequestResult


class UpdateMusicService:
    __music_api: MusicApi
    __music_repository: MusicRepository

    @inject
    def __init__(
            self,
            music_api: MusicApi = Provide[MusicInfraDependencyContainer.music_api],
            music_repository: MusicRepository = Provide[MusicInfraDependencyContainer.music_repository]
    ):
        self.__music_api = music_api
        self.__music_repository = music_repository

    def update_all_popularity_by_scheduler(self) -> None:
        all_music_list: list[Music] = self.__music_repository.get_all_music_list()
        for music in all_music_list:
            music_request_result: Optional[MusicRequestResult] = self.__music_api.get_music_by_music_id(music.music_id)
            if music_request_result is None:
                continue
            new_popularity: int = music_request_result.popularity
            music.update_popularity(new_popularity)
            self.__music_repository.update_music(music)
