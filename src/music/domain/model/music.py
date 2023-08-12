from src.common.domain.model.music_id_vo import MusicIdVO
from src.music.domain.model.cached_date_vo import CachedDateVO
from src.music.domain.model.lyrics_vo import LyricsVO
from src.music.domain.model.semantic_vo import SemanticVO
from src.music.domain.model.syntax_vo import SyntaxVO


class Music:
    __music_id: MusicIdVO
    __semantic: SemanticVO
    __syntax: SyntaxVO
    __lyrics: LyricsVO
    __cached_date: CachedDateVO

    def __init__(
            self,
            music_id: MusicIdVO,
            sematic: SemanticVO,
            syntax: SyntaxVO,
            lyrics: LyricsVO,
            cached_date: CachedDateVO
    ):
        self.__music_id = music_id
        self.__semantic = sematic
        self.__syntax = syntax
        self.__lyrics = lyrics
        self.__cached_date = cached_date

    @property
    def music_id(self):
        return self.__music_id

    @property
    def semantic(self):
        return self.__semantic

    @property
    def syntax(self):
        return self.__syntax

    @property
    def lyrics(self):
        return self.__lyrics

    @property
    def cached_date(self):
        return self.__cached_date
