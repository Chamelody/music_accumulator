from typing import Protocol

from src.semantic.domain.model.emotion_vo import EmotionVO
from src.semantic.domain.model.text_vo import TextVO


class SemanticExtractModel(Protocol):

    def extract_emotion(self, text: TextVO) -> EmotionVO:
        pass
