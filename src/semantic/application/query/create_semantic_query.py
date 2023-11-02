from dependency_injector.wiring import inject, Provide

from src.common.domain.model.music_id_vo import MusicIdVO
from src.common.domain.model.semantic_id_vo import SemanticIdVO
from src.config.di.semantic_dependency_container import SemanticDependencyContainer
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
            semantic_extract_model: SemanticExtractModel = Provide[SemanticDependencyContainer.semantic_extract_model],
            semantic_repository: SemanticRepository = Provide[SemanticDependencyContainer.semantic_repository]
    ):
        self.__semantic_extract_model = semantic_extract_model
        self.__semantic_repository = semantic_repository

    def create_and_save_semantic_by_text(self, semantic_id: SemanticIdVO, text: TextVO) -> Semantic:
        new_emotion: EmotionVO = self.__semantic_extract_model.extract_emotion(text)
        new_semantic: Semantic = Semantic(
            semantic_id=semantic_id,
            music_id=MusicIdVO(semantic_id.id),
            emotion=new_emotion,
            text=text
        )
        self.__semantic_repository.save_semantic(new_semantic)
        return new_semantic
