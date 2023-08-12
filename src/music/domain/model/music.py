from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.music.domain.model.cached_date_vo import CachedDateVO
from src.music.domain.model.lyrics_vo import LyricsVO


class Music:
    __music_id: MusicIdVO
    __semantic_id: SemanticIdVO
    __syntax_id: SyntaxIdVO
    __lyrics: LyricsVO
    __cached_date: CachedDateVO

    def __init__(
            self,
            music_id: MusicIdVO,
            sematic_id: SemanticIdVO,
            syntax_id: SyntaxIdVO,
            lyrics: LyricsVO,
            cached_date: CachedDateVO
    ):
        self.__music_id = music_id
        self.__semantic_id = sematic_id
        self.__syntax_id = syntax_id
        self.__lyrics = lyrics
        self.__cached_date = cached_date

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
    def lyrics(self) -> LyricsVO:
        return self.__lyrics

    @property
    def cached_date(self) -> CachedDateVO:
        return self.__cached_date
