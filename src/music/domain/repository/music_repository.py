from typing import Protocol, Optional

from src.common.domain.model.music_id_vo import MusicIdVO
from src.music.domain.model.music import Music


class MusicRepository(Protocol):

    def get_music_by_id(self, music_id: MusicIdVO) -> Optional[Music]:
        pass

    def get_all_music_list(self) -> list[Music]:
        pass

    def save_music(self, music: Music) -> bool:
        pass

    def update_music(self, music: Music) -> bool:
        pass

    def delete_music_by_id(self, music_id: MusicIdVO) -> bool:
        pass
