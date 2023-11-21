class MusicDto:
    def __init__(self, music_id: str, music_name: str, artists: list[str], music_image_url: str,
                 popularity: int, duration: int, lyrics: str,
                 happy: int, sad: int, fear: int, anger: int, love: int, danceability: float,
                 energy: float, music_key: int, loudness: float, mode: int, acousticness: float,
                 valence: float, tempo: float):
        self.__music_id = music_id
        self.__music_name = music_name
        self.__artists = artists
        self.__music_image_url = music_image_url
        self.__popularity = popularity
        self.__duration = duration
        self.__lyrics = lyrics
        self.__happy = happy
        self.__sad = sad
        self.__fear = fear
        self.__anger = anger
        self.__love = love
        self.__danceability = danceability
        self.__energy = energy
        self.__music_key = music_key
        self.__loudness = loudness
        self.__mode = mode
        self.__acousticness = acousticness
        self.__valence = valence
        self.__tempo = tempo

    def to_dict(self):
        return {
            "musicId": self.__music_id,
            "musicName": self.__music_name,
            "artists": self.__artists,
            "musicImageUrl": self.__music_image_url,
            "popularity": self.__popularity,
            "duration": self.__duration,
            "lyrics": self.__lyrics,
            "happy": self.__happy,
            "sad": self.__sad,
            "fear": self.__fear,
            "anger": self.__anger,
            "love": self.__love,
            "danceability": self.__danceability,
            "energy": self.__energy,
            "musicKey": self.__music_key,
            "loudness": self.__loudness,
            "mode": self.__mode,
            "acousticness": self.__acousticness,
            "valence": self.__valence,
            "tempo": self.__tempo
        }
