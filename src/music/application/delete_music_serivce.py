from src.common.domain.model.music_id_vo import MusicIdVO
from src.music.domain.repository.music_repository import MusicRepository


class DeleteMusicService:
    __music_repository: MusicRepository

    def __init__(self, music_repository: MusicRepository):
        self.__music_repository = music_repository

    def delete_music_by_id(self, music_id: MusicIdVO) -> bool:
        return self.__music_repository.delete_music_by_id(music_id)
