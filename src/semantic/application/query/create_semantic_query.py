from typing import Optional

from dependency_injector.wiring import inject, Provide

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.config.di.semantic_infra_dependency_container import SemanticInfraDependencyContainer
from src.semantic.domain.model.emotion_vo import EmotionVO
from src.semantic.domain.model.semantic import Semantic
from src.semantic.domain.model.text_vo import TextVO
from src.semantic.domain.repository.semantic_extract_model import SemanticExtractModel
from src.semantic.domain.repository.semantic_repository import SemanticRepository


class CreateSemanticQuery:

    __semantic_extract_model: SemanticExtractModel
    __semantic_repository: SemanticRepository

    @inject
    def __init__(
            self,
            semantic_extract_model: SemanticExtractModel = Provide[SemanticInfraDependencyContainer.semantic_extract_model],
            semantic_repository: SemanticRepository = Provide[SemanticInfraDependencyContainer.semantic_repository]
    ):
        self.__semantic_extract_model = semantic_extract_model
        self.__semantic_repository = semantic_repository

    def create_and_save_semantic_by_music_id(self, music_id: MusicIdVO, text: str) -> Semantic:
        new_semantic_id: SemanticIdVO = SemanticIdVO(music_id.id)
        semantic: Optional[Semantic] = self.__semantic_repository.get_semantic_by_id(new_semantic_id)
        if semantic is not None:
            return semantic
        new_text: TextVO = TextVO(text)
        new_emotion: EmotionVO = self.__semantic_extract_model.extract_emotion(new_text)
        new_semantic: Semantic = Semantic(
            semantic_id=new_semantic_id,
            music_id=MusicIdVO(music_id.id),
            emotion=new_emotion,
            text=new_text
        )
        self.__semantic_repository.save_semantic(new_semantic)
        return new_semantic
