from sqlalchemy import Column, String, Integer, Text, ForeignKey

from src.config.database.sqlalchemy_config import Base


class SemanticDO(Base):
    __tablename__ = 'semantic'
    # TODO Specify String length
    semantic_id = Column(String(), nullable=False, primary_key=True)
    music_id = Column(String(), ForeignKey('music.music_id'), nullable=False)
    happy = Column(Integer(), nullable=False)
    sad = Column(Integer(), nullable=False)
    fear = Column(Integer(), nullable=False)
    anger = Column(Integer(), nullable=False)
    love = Column(Integer(), nullable=False)
    text = Column(Text(), nullable=True)
