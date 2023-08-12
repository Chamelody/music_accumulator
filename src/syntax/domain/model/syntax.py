from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.syntax.domain.model.cached_date_vo import CachedDateVO
from src.syntax.domain.model.release_date_vo import ReleaseDateVO


class Syntax:
    __syntax_id: SyntaxIdVO
    __music_id: MusicIdVO  # Foreign Key
    __release_date: ReleaseDateVO
    __cached_date: CachedDateVO

    def __init__(
            self,
            syntax_id: SyntaxIdVO,
            music_id: MusicIdVO,
            release_date: ReleaseDateVO,
            cached_date: CachedDateVO
    ):
        self.__syntax_id = syntax_id
        self.__music_id = music_id
        self.__release_date = release_date
        self.__cached_date = cached_date

    @property
    def syntax_id(self):
        return self.__syntax_id

    @property
    def music_id(self):
        return self.__music_id

    @property
    def release_date(self):
        return self.__release_date

    @property
    def cached_date(self):
        return self.__cached_date
