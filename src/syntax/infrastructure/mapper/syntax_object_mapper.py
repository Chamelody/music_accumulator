from src.common.domain.model.cached_date_vo import CachedDateVO
from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.syntax.domain.model.feature_vo import FeatureVO
from src.syntax.domain.model.syntax import Syntax
from src.syntax.infrastructure.model.syntax_do import SyntaxDO


class SyntaxObjectMapper:

    @staticmethod
    def syntax_entity_to_do(syntax: Syntax) -> SyntaxDO:
        return SyntaxDO(
            syntax_id=syntax.syntax_id.id,
            music_id=syntax.music_id.id,
            danceability=syntax.feature.danceability,
            energy=syntax.feature.energy,
            music_key=syntax.feature.music_key,
            loudness=syntax.feature.loudness,
            mode=syntax.feature.mode,
            acousticness=syntax.feature.acousticness,
            valence=syntax.feature.valence,
            tempo=syntax.feature.tempo,
            cached_date=syntax.cached_date.cached_date
        )

    @staticmethod
    def syntax_do_to_entity(syntax_do: SyntaxDO) -> Syntax:
        return Syntax(
            syntax_id=SyntaxIdVO(syntax_do.syntax_id),
            music_id=MusicIdVO(syntax_do.music_id),
            feature=FeatureVO(
                danceability=syntax_do.danceability,
                energy=syntax_do.energy,
                music_key=syntax_do.music_key,
                loudness=syntax_do.loudness,
                mode=syntax_do.mode,
                acousticness=syntax_do.acousticness,
                valence=syntax_do.valence,
                tempo=syntax_do.tempo
            ),
            cached_date=CachedDateVO(syntax_do.cached_date)
        )
