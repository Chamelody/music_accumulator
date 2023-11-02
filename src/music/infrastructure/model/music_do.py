from sqlalchemy import Column, String, Integer, Date

from src.config.database.sqlalchemy_config import Base


class MusicDO(Base):
    __tablename__ = 'music'
    music_id = Column(String(), nullable=False, primary_key=True)
    semantic_id = Column(String(), nullable=False)
    syntax_id = Column(String(), nullable=False)
    music_name = Column(String(), nullable=False)
    artists = Column(String(), nullable=False)  # ex) name1,name2,name3, ...
    music_image_url = Column(String(), nullable=False)
    popularity = Column(Integer(), nullable=False)
    duration = Column(Integer(), nullable=False)
    lyrics = Column(String(), nullable=False)
    cached_date = Column(Date(), nullable=False)
    release_date = Column(Date(), nullable=False)
