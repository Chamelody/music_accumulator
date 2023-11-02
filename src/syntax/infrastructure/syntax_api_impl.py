from src.common.domain.model.music_id_vo import MusicIdVO
from src.syntax.domain.model.feature_vo import FeatureVO
from src.syntax.domain.repository.syntax_api import SyntaxApi


class SyntaxApiImpl(SyntaxApi):

    def get_feature_by_music_id(self, music_id: MusicIdVO) -> FeatureVO:
        pass
