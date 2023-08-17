from src.common.domain.model.music_id_vo import MusicIdVO
from src.music.domain.model.music import Music
from src.music.domain.repository.music_repository import MusicRepository


class ReadMusicService:
    __music_repository: MusicRepository

    def __init__(self, music_repository: MusicRepository):
        self.__music_repository = music_repository

    def get_music_by_id(self, music_id: MusicIdVO) -> Music:
        return self.__music_repository.get_music_by_id(music_id)

    def get_all_music(self) -> list[Music]:
        return self.__music_repository.get_all_music_list()
