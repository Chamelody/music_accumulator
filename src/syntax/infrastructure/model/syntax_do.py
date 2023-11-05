from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey

from src.config.database.sqlalchemy_config import Base


class SyntaxDO(Base):
    __tablename__ = 'syntax'
    # TODO Specify String length
    syntax_id = Column(String(), nullable=False, primary_key=True)
    music_id = Column(String(), ForeignKey('music.music_id'), nullable=False)
    danceability = Column(Float(), nullable=False)
    energy = Column(Float(), nullable=False)
    music_key = Column(Integer(), nullable=False)
    loudness = Column(Float(), nullable=False)
    mode = Column(Integer(), nullable=False)
    acousticness = Column(Float(), nullable=False)
    valence = Column(Float(), nullable=False)
    tempo = Column(Float(), nullable=False)
    cached_date = Column(Date(), nullable=False)
