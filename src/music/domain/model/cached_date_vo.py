from datetime import date


class CachedDateVO:
    __cached_date: date

    def __init__(self, cached_date: date):
        self.__cached_date = cached_date

    @property
    def cached_date(self) -> date:
        return self.__cached_date

    @classmethod
    def from_str(cls, date_str: str):
        """
        example: CachedDateVO.from_str("2023-8-12")
        """
        cls(date.fromisoformat(date_str))

    def __str__(self) -> str:
        return self.cached_date.__str__()
