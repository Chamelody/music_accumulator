class MusicRequestResult:
    __music_id: str
    __music_name: str
    __artists: list[str]
    __music_image_url: str
    __popularity: int
    __duration: int
    __lyrics: str

    def __init__(
            self,
            music_id: str,
            music_name: str,
            artists: list[str],
            music_image_url: str,
            popularity: int,
            duration: int,
            lyrics: str
    ):
        self.__music_id = music_id
        self.__music_name = music_name
        self.__artists = artists
        self.__music_image_url = music_image_url
        self.__popularity = popularity
        self.__duration = duration
        self.__lyrics = lyrics

    @property
    def music_id(self) -> str:
        return self.__music_id

    @property
    def music_name(self) -> str:
        return self.__music_name

    @property
    def artists(self) -> list[str]:
        return self.__artists

    @property
    def music_image_url(self) -> str:
        return self.__music_image_url

    @property
    def popularity(self) -> int:
        return self.__popularity

    @property
    def duration(self) -> int:
        return self.__duration

    @property
    def lyrics(self) -> str:
        return self.__lyrics
