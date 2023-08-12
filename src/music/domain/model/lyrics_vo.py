class LyricsVO:
    __lyrics: str

    def __init__(self, lyrics: str):
        self.__lyrics = lyrics

    @property
    def lyrics(self) -> str:
        return self.__lyrics

    def __str__(self) -> str:
        return self.lyrics
