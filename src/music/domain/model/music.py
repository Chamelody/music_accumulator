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
