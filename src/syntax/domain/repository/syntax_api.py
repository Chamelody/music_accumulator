from typing import Protocol

from src.common.domain.model.music_id_vo import MusicIdVO
from src.syntax.domain.model.feature_vo import FeatureVO


class SyntaxApi(Protocol):

    def get_feature_by_music_id(self, music_id: MusicIdVO) -> FeatureVO:
        pass
