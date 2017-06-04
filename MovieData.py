from Exceptions import NoDataEXC, ResponseEXC
import requests


class MovieData:

    api_key_v3 = "a2fc9a9514e82dfd0f6281eab939459d"
    request = ""
    downloaded = False

    data = ""

    def create_request(self, show_type, name):
        name_list = name.split()
        new_name = '+'.join(name_list)
        if show_type == "movie":
            self.request = "http://api.themoviedb.org/3/search/movie" + "?api_key=" \
                           + self.api_key_v3 + "&query=" + new_name
        else:
            self.request = "http://api.themoviedb.org/3/search/tv" + "?api_key=" \
                           + self.api_key_v3 + "&query=" + new_name

    def get_title(self):
        return self.data.get("results")[0].get("title")

    def get_vote_average(self):
        return float(self.data.get("results")[0].get("vote_average"))

    def get_vote_count(self):
        return int(self.data.get("results")[0].get("vote_count"))

    def get_popularity(self):
        return float(self.data.get("results")[0].get("popularity"))

    def get_name(self):
        return self.data.get("results")[0].get("name")

    def get_data(self):

        response = requests.get(self.request)
        self.check_status(response)
        json_data = response.json()
        self.check_data(json_data)
        self.data = json_data

    def check_status(self, response):
        if response.status_code != 200:
            raise ResponseEXC("Response Error\n")

    def check_data(self, data):
        if len(data.get("results")) == 0:
            raise NoDataEXC("Content Error\n")
