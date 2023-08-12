from flask import Flask
from src.music.presentation.music_controller import music_controller


app = Flask(__name__)
app.register_blueprint(music_controller)


if __name__ == '__main__':
    app.run()
