class EmotionVO:
    __happy: int
    __sad: int
    __fear: int
    __anger: int
    __love: int

    def __init__(self, happy: int, sad: int, fear: int, anger: int, love: int):
        total_emotion_value: int = happy + sad + fear + anger + love
        if total_emotion_value != 100:
            raise RuntimeError("Total emotion value is not 100,", total_emotion_value)

        self.__happy = happy
        self.__sad = sad
        self.__fear = fear
        self.__anger = anger
        self.__love = love

    @property
    def happy(self) -> int:
        return self.__happy

    @property
    def sad(self) -> int:
        return self.__sad

    @property
    def fear(self) -> int:
        return self.__fear

    @property
    def anger(self) -> int:
        return self.__anger

    @property
    def love(self) -> int:
        return self.__love
