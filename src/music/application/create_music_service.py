from dependency_injector.wiring import inject, Provide

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.release_date_vo import ReleaseDateVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.config.di.music_dependency_container import MusicDependencyContainer
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

    @inject
    def __init__(
            self,
            music_repository: MusicRepository = Provide[MusicDependencyContainer.music_repository],
            music_api: MusicApi = Provide[MusicDependencyContainer.music_api],
            syntax_query: SyntaxQuery = Provide[MusicDependencyContainer.syntax_query],
            semantic_query: SemanticQuery = Provide[MusicDependencyContainer.semantic_query]
    ):
        self.__music_repository = music_repository
        self.__music_api = music_api
        self.__syntax_query = syntax_query
        self.__semantic_query = semantic_query

    def create_and_save_music_by_id(self, music_id: MusicIdVO) -> Music:
        music_request_result: MusicRequestResult = self.__music_api.get_music_by_music_id(music_id)
        new_music_id: MusicIdVO = MusicIdVO(music_request_result.music_id)
        new_lyrics: LyricsVO = LyricsVO(music_request_result.lyrics)
        release_date: ReleaseDateVO = ReleaseDateVO(music_request_result.release_date)
        syntax_id: SyntaxIdVO = self.__syntax_query.create_syntax_by_music_id(new_music_id)
        semantic_id: SemanticIdVO = self.__semantic_query.create_semantic(new_music_id, new_lyrics)
        new_music: Music = Music(
            music_id=new_music_id,
            semantic_id=semantic_id,
            syntax_id=syntax_id,
            music_name=music_request_result.music_name,
            artists=music_request_result.artists,
            music_image_url=music_request_result.music_image_url,
            popularity=music_request_result.popularity,
            duration=music_request_result.duration,
            lyrics=new_lyrics,
            cached_date=None,
            release_date=release_date
        )
        self.__music_repository.save_music(new_music)
        return new_music

    def create_and_save_music_list_by_playlist_id(self, playlist_id: str) -> list[Music]:
        music_id_list: list[MusicIdVO] = self.__music_api.get_music_id_list_by_playlist_id(playlist_id)
        music_list: list[Music] = [self.create_and_save_music_by_id(music_id) for music_id in music_id_list]
        # map(lambda music: self.__music_repository.save_music(music), music_list)
        return music_list
