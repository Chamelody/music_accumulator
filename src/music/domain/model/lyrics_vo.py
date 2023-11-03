from typing import Optional


class LyricsVO:
    __lyrics: Optional[str]

    def __init__(self, lyrics: Optional[str]):
        self.__lyrics = lyrics

    @property
    def lyrics(self) -> Optional[str]:
        return self.__lyrics

    def __str__(self) -> str:
        if self.lyrics is None:
            return "None"
        return self.lyrics
