from dependency_injector.wiring import inject, Provide
from flask import Blueprint

from src.common.domain.model.music_id_vo import MusicIdVO
from src.config.di.music_app_dependency_container import MusicAppDependencyContainer
from src.music.application.create_music_service import CreateMusicService

music_controller = Blueprint('music_controller', __name__, url_prefix='/music')


@music_controller.route("/")
def main():
    return "Hello, world!"


@music_controller.route("/add_track/<track_id>")
@inject
def add_track(
        track_id: str,
        create_music_service: CreateMusicService = Provide[MusicAppDependencyContainer.create_music_service]
):
    create_music_service.create_and_save_music_by_id(MusicIdVO(track_id))
    # TODO return music dto.
    return "200"


@music_controller.route("/add_playlist/<playlist_id>")
@inject
def add_playlist(
    playlist_id: str,
    create_music_service: CreateMusicService = Provide[MusicAppDependencyContainer.create_music_service]
):
    create_music_service.create_and_save_music_list_by_playlist_id(playlist_id)
    # TODO return music dto list.
    return "200"
