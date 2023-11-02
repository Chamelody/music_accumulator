from src.common.domain.model.music_id_vo import MusicIdVO
from src.music.domain.model.music import Music
from src.music.domain.repository.music_repository import MusicRepository


class MusicRepositoryImpl(MusicRepository):

    def get_music_by_id(self, music_id: MusicIdVO) -> Music:
        pass

    def get_all_music_list(self) -> list[Music]:
        pass

    def save_music(self, music: Music) -> bool:
        pass

    def update_music(self, music: Music) -> bool:
        pass

    def delete_music_by_id(self, music_id: MusicIdVO) -> bool:
        pass
