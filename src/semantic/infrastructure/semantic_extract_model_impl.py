from src.semantic.domain.model.emotion_vo import EmotionVO
from src.semantic.domain.model.text_vo import TextVO
from src.semantic.domain.repository.semantic_extract_model import SemanticExtractModel


class SemanticExtractModelImpl(SemanticExtractModel):

    def extract_emotion(self, text: TextVO) -> EmotionVO:
        # TODO implement this.
        return EmotionVO(
            happy=20,
            sad=20,
            fear=20,
            anger=20,
            love=20
        )
