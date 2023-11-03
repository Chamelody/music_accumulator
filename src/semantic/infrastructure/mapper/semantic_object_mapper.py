from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.semantic.domain.model.emotion_vo import EmotionVO
from src.semantic.domain.model.semantic import Semantic
from src.semantic.domain.model.text_vo import TextVO
from src.semantic.infrastructure.model.semantic_do import SemanticDO


class SemanticObjectMapper:

    @staticmethod
    def semantic_entity_to_do(semantic: Semantic) -> SemanticDO:
        return SemanticDO(
            semantic_id=semantic.semantic_id.id,
            music_id=semantic.music_id.id,
            happy=semantic.emotion.happy,
            sad=semantic.emotion.sad,
            fear=semantic.emotion.fear,
            anger=semantic.emotion.anger,
            love=semantic.emotion.love,
            text=semantic.text.text
        )

    @staticmethod
    def semantic_do_to_entity(semantic_do: SemanticDO) -> Semantic:
        return Semantic(
            semantic_id=SemanticIdVO(semantic_do.semantic_id),
            music_id=MusicIdVO(semantic_do.music_id),
            emotion=EmotionVO(
                happy=semantic_do.happy,
                sad=semantic_do.sad,
                fear=semantic_do.fear,
                anger=semantic_do.anger,
                love=semantic_do.love
            ),
            text=TextVO(semantic_do.text)
        )
