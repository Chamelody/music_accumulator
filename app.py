from flask import Flask
from dotenv import load_dotenv

load_dotenv()


from src.config.database.sqlalchemy_config import Base, engine
from src.music.presentation.music_controller import music_controller

from src.music.infrastructure.model.music_do import MusicDO  # To load data object first
from src.semantic.infrastructure.model.semantic_do import SemanticDO  # To load data object first
from src.syntax.infrastructure.model.syntax_do import SyntaxDO  # To load data object first


Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.register_blueprint(blueprint=music_controller)


if __name__ == '__main__':
    app.run()
