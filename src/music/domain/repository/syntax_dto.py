class SyntaxDto:
    __danceability: float
    __energy: float
    __music_key: int
    __loudness: float
    __mode: int
    __acousticness: float
    __valence: float
    __tempo: float

    def __init__(
            self,
            danceability: float,
            energy: float,
            music_key: int,
            loudness: float,
            mode: int,
            acousticness: float,
            valence: float,
            tempo: float
    ):
        self.__danceability = danceability
        self.__energy = energy
        self.__music_key = music_key
        self.__loudness = loudness
        self.__mode = mode
        self.__acousticness = acousticness
        self.__valence = valence
        self.__tempo = tempo

    @property
    def danceability(self) -> float:
        return self.__danceability

    @property
    def energy(self) -> float:
        return self.__energy

    @property
    def music_key(self) -> int:
        return self.__music_key

    @property
    def loudness(self) -> float:
        return self.__loudness

    @property
    def mode(self) -> int:
        return self.__mode

    @property
    def acousticness(self) -> float:
        return self.__acousticness

    @property
    def valence(self) -> float:
        return self.__valence

    @property
    def tempo(self) -> float:
        return self.__tempo
