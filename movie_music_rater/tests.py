import pytest
from movie_music_rater.movie_data import MovieData
from movie_music_rater.music_data import MusicData

from movie_music_rater.exceptions import ResponseEXC, NoDataEXC


class Tests:

    def __init__(self):
        pass

    movie_data = MovieData()
    music_data = MusicData()

    def test_get_movie_data(self):
        with pytest.raises(NoDataEXC):
            self.movie_data.create_request("movie", "should throw no data exception")
            self.movie_data.get_data()

    def test_get_music_data(self):
        with pytest.raises(NoDataEXC):
            self.music_data.get_similar("also should throw no data exception")

    def test_get_music_data2(self):
        with pytest.raises(NoDataEXC):
            self.music_data.get_top_songs("and also here should throw no data exception")

    def test_get_music_data3(self):
        with pytest.raises(NoDataEXC):
            self.music_data.get_involvement_factor("should throw no data exception")

    def test_wrong_api_movie(self):
        with pytest.raises(ResponseEXC):
            self.movie_data.api_key_v3 = "again should throw no data exception"

