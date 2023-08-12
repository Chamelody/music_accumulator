from datetime import date


class ReleaseDateVO:
    __release_date: date

    def __init__(self, release_date: date):
        self.__release_date = release_date

    @property
    def release_date(self) -> date:
        return self.__release_date

    @classmethod
    def from_str(cls, date_str: str):
        """
        example: ReleaseDateVO.from_str("2023-8-12")
        """
        cls(date.fromisoformat(date_str))

    def __str__(self) -> str:
        return self.release_date.__str__()
