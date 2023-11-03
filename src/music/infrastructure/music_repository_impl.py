from typing import Optional

from sqlalchemy.exc import SQLAlchemyError

from src.common.domain.model.music_id_vo import MusicIdVO
from src.config.database.sqlalchemy_config import session
from src.music.domain.model.music import Music
from src.music.domain.repository.music_repository import MusicRepository
from src.music.infrastructure.mapper.music_object_mapper import MusicObjectMapper
from src.music.infrastructure.model.music_do import MusicDO


class MusicRepositoryImpl(MusicRepository):

    def get_music_by_id(self, music_id: MusicIdVO) -> Optional[Music]:
        try:
            music_do: MusicDO = session.query(MusicDO).filter(MusicDO.music_id == music_id.id).first()
            if music_do is None:
                return None
            return MusicObjectMapper.music_do_to_entity(music_do)
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            return None

    def get_all_music_list(self) -> list[Music]:
        try:
            all_music_do: list[MusicDO] = session.query(MusicDO).all()
            return list(map(MusicObjectMapper.music_do_to_entity, all_music_do))
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            return []

    def save_music(self, music: Music) -> bool:
        music_do: MusicDO = MusicObjectMapper.music_entity_to_do(music)
        try:
            session.add(music_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False

    def update_music(self, music: Music) -> bool:
        try:
            music_do: MusicDO = session.query(MusicDO).filter(MusicDO.music_id == music.music_id.id).first()
            session.add(music_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False

    def delete_music_by_id(self, music_id: MusicIdVO) -> bool:
        try:
            music_do: MusicDO = session.query(MusicDO).filter(MusicDO.music_id == music_id.id).first()
            session.delete(music_do)
            session.commit()
            return True
        except SQLAlchemyError as e:
            print(f"SQL Error: {e}")
            session.rollback()
            return False
