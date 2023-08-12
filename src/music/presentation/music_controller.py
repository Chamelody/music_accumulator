from flask import Blueprint


music_controller = Blueprint('music_controller', __name__, url_prefix='/music')


@music_controller.route("/")
def main():
    return "Hello, world!"
