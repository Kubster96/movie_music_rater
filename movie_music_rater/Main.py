from movie_music_rater.MovieData import MovieData
from movie_music_rater.MusicData import MusicData

from movie_music_rater.Exceptions import NoDataEXC, ResponseEXC

# messages

info_type = "Choose type of info form available types: \n" \
            "movie\n" \
            "tv_series\n" \
            "music\n"

info_name = "Choose name of movie or tv_series or artist name\n"

info_continue = "Do you want to continue (y/n)? \n"


def main():

    working = True
    error = False

    while working:
        type = input(info_type)
        print(type)
        name = input(info_name)
        music_data = MusicData()
        movie_data = MovieData()

        if type != "music":
            movie_data.create_request(type, name)
            try:
                movie_data.get_data()
            except ResponseEXC:
                print("Response Error\n")
                error = True

            except NoDataEXC:
                print("No Data Error\n")
                error = True

        else:

            try:
                music_data.get_top_songs(name)
                music_data.get_similar(name)
                music_data.get_involvement_factor(name)

            except ResponseEXC:
                print("Response Error\n")
                error = True

            except NoDataEXC:
                print("No Data Error\n")
                error = True

        if not error:

            if type != "music":
                if type == "movie":
                    print("Movie")
                    print("Title: " + movie_data.get_title())
                else:
                    print("TV series")
                    print("Title: " + movie_data.get_name())

                print("Vote average: " + str(movie_data.get_vote_average()))
                print("Vote count: " + str(movie_data.get_vote_count()))
                print("Popularity: " + str(movie_data.get_popularity()))
                print("Worth watching factor: " + str((movie_data.get_vote_count()*movie_data.get_popularity())/
                                                      (10 - movie_data.get_vote_average())))

            else:
                print("Music")
                print(name)
                print("Similar artists: ")
                print_list(music_data.similar)
                print("Top songs: ")
                print_list(music_data.top_song)
                print("Genres: ")
                print_list(music_data.genres)
                print("Involvement factor (scrobbles per listener): " + str(music_data.involvement_factor))


        working = input(info_continue) == 'y'


def print_list(elements):
    for i in elements:
        print("\t - " + i)

if __name__ == "__main__":
    main()
