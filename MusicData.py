import requests
from Exceptions import NoDataEXC, ResponseEXC
from itertools import islice


class MusicData:

    api_key = "fa79514efe98769c82ba5fca5256c6b6"
    similar = []
    top_song = []

    def get_similar(self, artist):
        artist_list = artist.split()
        new_artist = ''.join(artist_list)

        request = "http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=" + new_artist + "&api_key=" \
                  + self.api_key + "&format=json"

        response = requests.get(request)
        self.check_status(response)

        json_data = response.json()
        self.check_data(json_data)

        for i in islice(json_data.get("similarartists").get("artist"), 5):
            self.similar.append(i.get("name"))

    def get_top_songs(self, artist):
        artist_list = artist.split()
        new_artist = ''.join(artist_list)

        request = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=" + new_artist + "&api_key=" \
                  + self.api_key + "&format=json"

        response = requests.get(request)
        self.check_status(response)

        json_data = response.json()
        self.check_data(json_data)

        for i in islice(json_data.get("toptracks").get("track"), 10):
            self.top_song.append(i.get("name"))

    def check_status(self, response):
        if response.status_code != 200:
            raise ResponseEXC("Response Error\n")

    def check_data(self, data):
        if data is None:
            raise NoDataEXC("Content Error\n")
