from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.semantic.domain.model.emotion_vo import EmotionVO
from src.semantic.domain.model.text_vo import TextVO


class Semantic:
    __semantic_id: SemanticIdVO
    __music_id: MusicIdVO  # Foreign Key
    __emotion: EmotionVO
    __text: TextVO

    def __init__(self, sematic_id: SemanticIdVO, music_id: MusicIdVO, emotion: EmotionVO, text: TextVO):
        self.__semantic_id = sematic_id
        self.__music_id = music_id
        self.__emotion = emotion
        self.__text = text

    @property
    def semantic_id(self) -> SemanticIdVO:
        return self.__semantic_id

    @property
    def music_id(self) -> MusicIdVO:
        return self.__music_id

    @property
    def emotion(self) -> EmotionVO:
        return self.__emotion

    @property
    def text(self) -> TextVO:
        return self.__text
