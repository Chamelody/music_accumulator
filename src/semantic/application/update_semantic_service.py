from src.semantic.domain.model.emotion_vo import EmotionVO
from src.semantic.domain.model.semantic import Semantic
from src.semantic.domain.repository.semantic_extract_model import SemanticExtractModel
from src.semantic.domain.repository.semantic_repository import SemanticRepository


class UpdateSemanticService:

    __semantic_extract_model: SemanticExtractModel
    __semantic_repository: SemanticRepository

    def __init__(self, semantic_extract_model: SemanticExtractModel, semantic_repository: SemanticRepository):
        self.__semantic_extract_model = semantic_extract_model
        self.__semantic_repository = semantic_repository

    def update_all_emotion(self) -> None:
        all_semantics: list[Semantic] = self.__semantic_repository.get_all_semantics()
        for semantic in all_semantics:
            new_emotion: EmotionVO = self.__semantic_extract_model.extract_emotion(semantic.text)
            semantic.update_emotion(new_emotion)
            self.__semantic_repository.update_semantic(semantic)
