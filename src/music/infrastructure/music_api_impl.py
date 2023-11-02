from src.common.domain.model.music_id_vo import MusicIdVO
from src.music.domain.repository.music_api import MusicApi
from src.music.domain.repository.music_request_result import MusicRequestResult


class MusicApiImpl(MusicApi):

    def get_music_by_music_id(self, music_id: MusicIdVO) -> MusicRequestResult:
        pass

    def get_music_id_list_by_playlist_id(self, playlist_id: str) -> list[MusicIdVO]:
        pass
