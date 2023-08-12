from typing import Protocol

from src.music.domain.repository.music_request_result import MusicRequestResult


class MusicApi(Protocol):

    def get_music_by_music_id(self, music_id: str) -> MusicRequestResult:
        pass

    def get_music_id_list_by_playlist_id(self, playlist_id: str) -> list[str]:
        pass
