from src.common.domain.model.cached_date_vo import CachedDateVO
from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.release_date_vo import ReleaseDateVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.music.domain.model.lyrics_vo import LyricsVO
from src.music.domain.model.music import Music
from src.music.infrastructure.model.music_do import MusicDO


class MusicObjectMapper:

    @staticmethod
    def music_entity_to_do(music: Music) -> MusicDO:
        return MusicDO(
            music_id=music.music_id.id,
            semantic_id=music.semantic_id.id,
            syntax_id=music.syntax_id.id,
            music_name=music.music_name,
            artists=','.join(music.artists),
            music_image_url=music.music_image_url,
            popularity=music.popularity,
            duration=music.duration,
            lyrics=music.lyrics.lyrics,
            cached_date=music.cached_date.cached_date,
            release_date=music.release_date.release_date
        )

    @staticmethod
    def music_do_to_entity(music_do: MusicDO) -> Music:
        return Music(
            music_id=MusicIdVO(music_do.music_id),
            semantic_id=SemanticIdVO(music_do.semantic_id),
            syntax_id=SyntaxIdVO(music_do.syntax_id),
            music_name=music_do.music_name,
            artists=music_do.split(','),
            music_image_url=music_do.music_image_url,
            popularity=music_do.popularity,
            duration=music_do.duration,
            lyrics=LyricsVO(music_do.lyrics),
            cached_date=CachedDateVO(music_do.cached_date),
            release_date=ReleaseDateVO(music_do.release_date)
        )
