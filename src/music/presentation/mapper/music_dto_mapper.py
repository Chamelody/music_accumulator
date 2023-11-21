from src.music.application.read_music_service import music_information_type
from src.music.domain.model.music import Music
from src.music.domain.repository.semantic_dto import SemanticDto
from src.music.domain.repository.syntax_dto import SyntaxDto
from src.music.presentation.model.music_dto import MusicDto


class MusicDtoMapper:

    @staticmethod
    def music_information_to_dto(music_information: music_information_type) -> MusicDto:
        music: Music = music_information[0]
        syntax_dto: SyntaxDto = music_information[1]
        semantic_dto: SemanticDto = music_information[2]
        return MusicDto(
            music_id=music.music_id.id,
            music_name=music.music_name,
            artists=music.artists,
            music_image_url=music.music_image_url,
            popularity=music.popularity,
            duration=music.duration,
            lyrics=music.lyrics.lyrics,
            happy=semantic_dto.happy,
            sad=semantic_dto.sad,
            fear=semantic_dto.fear,
            anger=semantic_dto.anger,
            love=semantic_dto.love,
            danceability=syntax_dto.danceability,
            energy=syntax_dto.energy,
            music_key=syntax_dto.music_key,
            loudness=syntax_dto.loudness,
            mode=syntax_dto.mode,
            acousticness=syntax_dto.acousticness,
            valence=syntax_dto.valence,
            tempo=syntax_dto.tempo
        )
