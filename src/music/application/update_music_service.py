from src.music.domain.model.music import Music
from src.music.domain.repository.music_api import MusicApi
from src.music.domain.repository.music_repository import MusicRepository
from src.music.domain.repository.music_request_result import MusicRequestResult


class UpdateMusicService:
    __music_api: MusicApi
    __music_repository: MusicRepository

    def __init__(self, music_api: MusicApi, music_repository: MusicRepository):
        self.__music_api = music_api
        self.__music_repository = music_repository

    def update_all_popularity_by_scheduler(self) -> None:
        all_music_list: list[Music] = self.__music_repository.get_all_music_list()
        for music in all_music_list:
            music_request_result: MusicRequestResult = self.__music_api.get_music_by_music_id(music.music_id)
            new_popularity: int = music_request_result.popularity
            music.update_popularity(new_popularity)
            self.__music_repository.update_music(music)
