from src.common.domain.model.cached_date_vo import CachedDateVO
from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.syntax.domain.model.feature_vo import FeatureVO


class Syntax:
    __syntax_id: SyntaxIdVO
    __music_id: MusicIdVO  # Foreign Key
    __feature: FeatureVO
    __popularity: int
    __cached_date: CachedDateVO

    def __init__(
            self,
            syntax_id: SyntaxIdVO,
            music_id: MusicIdVO,
            feature: FeatureVO,
            popularity: int,
            cached_date: CachedDateVO
    ):
        self.__syntax_id = syntax_id
        self.__music_id = music_id
        self.__feature = feature
        self.__popularity = popularity
        self.__cached_date = cached_date

    @property
    def syntax_id(self) -> SyntaxIdVO:
        return self.__syntax_id

    @property
    def music_id(self) -> MusicIdVO:
        return self.__music_id

    @property
    def feature(self) -> FeatureVO:
        return self.__feature

    @property
    def popularity(self) -> int:
        return self.__popularity

    @property
    def cached_date(self) -> CachedDateVO:
        return self.__cached_date
