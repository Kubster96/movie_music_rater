import pytest
from movie_music_rater.MovieData import MovieData
from movie_music_rater.MusicData import MusicData

from movie_music_rater.Exceptions import ResponseEXC, NoDataEXC


class Tests:

    movie_data = MovieData()
    music_data = MusicData()

    def test_get_movie_data(self):
        with pytest.raises(NoDataEXC):
            self.movie_data.create_request("movie", "dsadasdasdadas")
            self.movie_data.get_data()

    def test_get_music_data(self):
        with pytest.raises(NoDataEXC):
            self.music_data.get_similar("asdasdasda")

    def test_get_music_data2(self):
        with pytest.raises(NoDataEXC):
            self.music_data.get_top_songs("dasdasdasdasdad")

    def test_get_music_data3(self):
        with pytest.raises(NoDataEXC):
            self.music_data.get_involvement_factor("dasdasdasdadsad")

    def test_wrong_api_movie(self):
        with pytest.raises(ResponseEXC):
            self.movie_data.api_key_v3 = "lalalala"

    def test_wrong_api_music(self):
        with pytest.raises(ResponseEXC):
            self.music_data.api_key = "lalalala"
