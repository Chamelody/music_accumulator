from datetime import date

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.common.domain.model.cached_date_vo import CachedDateVO
from src.music.domain.model.lyrics_vo import LyricsVO
from src.common.domain.model.release_date_vo import ReleaseDateVO


class Music:
    __music_id: MusicIdVO
    __semantic_id: SemanticIdVO
    __syntax_id: SyntaxIdVO
    __music_name: str
    __artists: list[str]
    __music_image_url: str
    __popularity: int
    __duration: int
    __lyrics: LyricsVO
    __cached_date: CachedDateVO
    __release_date: ReleaseDateVO

    def __init__(
            self,
            music_id: MusicIdVO,
            sematic_id: SemanticIdVO,
            syntax_id: SyntaxIdVO,
            music_name: str,
            artists: list[str],
            music_image_url: str,
            popularity: int,
            duration: int,
            lyrics: LyricsVO,
            release_date: ReleaseDateVO
    ):
        self.__music_id = music_id
        self.__semantic_id = sematic_id
        self.__syntax_id = syntax_id
        self.__music_name = music_name
        self.__artists = artists
        self.__music_image_url = music_image_url
        self.__popularity = popularity
        self.__duration = duration
        self.__lyrics = lyrics
        self.__cached_date = CachedDateVO(date.today())
        self.__release_date = release_date

    def update_popularity(self, new_popularity: int) -> None:
        self.__popularity = new_popularity

    @property
    def music_id(self) -> MusicIdVO:
        return self.__music_id

    @property
    def semantic(self) -> SemanticIdVO:
        return self.__semantic_id

    @property
    def syntax(self) -> SyntaxIdVO:
        return self.__syntax_id

    @property
    def music_name(self) -> str:
        return self.__music_name

    @property
    def artists(self) -> list[str]:
        return self.__artists

    @property
    def music_image_url(self) -> str:
        return self.__music_image_url

    @property
    def popularity(self) -> int:
        return self.__popularity

    @property
    def duration(self) -> int:
        return self.__duration

    @property
    def lyrics(self) -> LyricsVO:
        return self.__lyrics

    @property
    def cached_date(self) -> CachedDateVO:
        return self.__cached_date

    @property
    def release_date(self) -> ReleaseDateVO:
        return self.__release_date
