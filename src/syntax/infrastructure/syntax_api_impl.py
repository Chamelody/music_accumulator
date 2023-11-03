from src.common.domain.model.music_id_vo import MusicIdVO
from src.config.api.spotipy_config import sp
from src.syntax.domain.model.feature_vo import FeatureVO
from src.syntax.domain.repository.syntax_api import SyntaxApi


class SyntaxApiImpl(SyntaxApi):

    def get_feature_by_music_id(self, music_id: MusicIdVO) -> FeatureVO:
        audio_features = sp.audio_features(music_id.id)[0]
        return FeatureVO(
            danceability=audio_features['danceability'],
            energy=audio_features['energy'],
            music_key=audio_features['key'],
            loudness=audio_features['loudness'],
            mode=audio_features['mode'],
            acousticness=audio_features['acousticness'],
            valence=audio_features['valence'],
            tempo=audio_features['tempo']
        )
