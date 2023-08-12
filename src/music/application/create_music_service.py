from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.release_date_vo import ReleaseDateVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.music.domain.model.lyrics_vo import LyricsVO
from src.music.domain.model.music import Music
from src.music.domain.repository.music_api import MusicApi
from src.music.domain.repository.music_repository import MusicRepository
from src.music.domain.repository.music_request_result import MusicRequestResult
from src.music.domain.repository.semantic_query import SemanticQuery
from src.music.domain.repository.syntax_query import SyntaxQuery


class CreateMusicService:
    __music_repository: MusicRepository
    __music_api: MusicApi
    __syntax_query: SyntaxQuery
    __semantic_query: SemanticQuery

    def __init__(self, music_repository: MusicRepository, music_api: MusicApi):
        self.__music_repository = music_repository
        self.__music_api = music_api

    def create_music_by_id(self, music_id: str) -> Music:
        music_request_result: MusicRequestResult = self.__music_api.get_music_by_music_id(music_id)
        new_music_id: MusicIdVO = MusicIdVO(music_request_result.music_id)
        new_lyrics: LyricsVO = LyricsVO(music_request_result.lyrics)
        release_date: ReleaseDateVO = ReleaseDateVO(music_request_result.release_date)
        syntax_id: SyntaxIdVO = self.__syntax_query.create_syntax_by_music_id(new_music_id)
        semantic_id: SemanticIdVO = self.__semantic_query.create_semantic(new_lyrics)
        return Music(
            music_id=new_music_id,
            sematic_id=semantic_id,
            syntax_id=syntax_id,
            music_name=music_request_result.music_name,
            artists=music_request_result.artists,
            music_image_url=music_request_result.music_image_url,
            popularity=music_request_result.popularity,
            duration=music_request_result.duration,
            lyrics=new_lyrics,
            release_date=release_date
        )

    def create_music_list_by_playlist_id(self, playlist_id: str) -> list[Music]:
        music_id_list: list[str] = self.__music_api.get_music_id_list_by_playlist_id(playlist_id)
        music_list: list[Music] = [self.create_music_by_id(music_id) for music_id in music_id_list]
        return music_list
    