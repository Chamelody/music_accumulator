from typing import Protocol

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.music.domain.repository.syntax_dto import SyntaxDto


class SyntaxQuery(Protocol):

    def create_syntax_by_music_id(self, music_id: MusicIdVO) -> SyntaxIdVO:
        pass

    def get_syntax_by_id(self, syntax_id: SyntaxIdVO) -> SyntaxDto:
        pass
