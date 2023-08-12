from src.common.domain.model.syntax_id_vo import SyntaxIdVO
from src.syntax.domain.model.cached_date_vo import CachedDateVO
from src.syntax.domain.model.release_date_vo import ReleaseDateVO


class Syntax:
    __syntax_id: SyntaxIdVO
    __release_date: ReleaseDateVO
    __cached_date: CachedDateVO
