from datetime import date, datetime

import json
from typing import Optional

import requests
from requests import RequestException
from spotipy import SpotifyException

from src.common.domain.model.music_id_vo import MusicIdVO
from src.config.api.spotipy_config import sp
from src.music.domain.repository.music_api import MusicApi
from src.music.domain.repository.music_request_result import MusicRequestResult


class MusicApiImpl(MusicApi):

    # Temporary measure
    SPOTIFY_LYRICS_API_URL = "https://spotify-lyric-api-984e7b4face0.herokuapp.com/?trackid="

    def get_lyrics(self, music_id: MusicIdVO) -> Optional[str]:
        try:
            res = requests.get(f"{self.SPOTIFY_LYRICS_API_URL}{music_id.id}")
        except RequestException as e:
            print(f"API ERROR: {e}")
            return None
        json_data = json.loads(res.text)
        if 'lines' not in json_data:
            return None
        lyrics_lines = json_data['lines']
        lyrics: str = ""
        for line in lyrics_lines:
            lyrics += line['words'] + "\n"
        return lyrics

    def get_music_by_music_id(self, music_id: MusicIdVO) -> Optional[MusicRequestResult]:
        try:
            track = sp.track(track_id=music_id.id)
        except SpotifyException as e:
            print(f"API ERROR: {e}")
            return None
        new_music_id: str = track['id']
        music_name: str = track['name']
        artists: list[str] = [artist['name'] for artist in track['artists']]
        music_image_url: str = track['album']['images'][0]['url']
        popularity: int = track['popularity']
        duration: int = track['duration_ms']
        lyrics: str = self.get_lyrics(music_id)
        release_date: date = datetime.strptime(track['album']['release_date'], "%Y-%m-%d").date()

        return MusicRequestResult(
            music_id=new_music_id,
            music_name=music_name,
            artists=artists,
            music_image_url=music_image_url,
            popularity=popularity,
            duration=duration,
            lyrics=lyrics,
            release_date=release_date
        )

    def get_music_id_list_by_playlist_id(self, playlist_id: str) -> list[MusicIdVO]:
        try:
            playlist = sp.playlist(playlist_id=playlist_id)
        except SpotifyException as e:
            print(f"API ERROR: {e}")
            return []
        items = playlist['tracks']['items']
        music_id_list: list[MusicIdVO] = list()
        for item in items:
            track = item['track']
            music_id_list.append(MusicIdVO(track['id']))
        return music_id_list
