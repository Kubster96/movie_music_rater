
# messages

info_type = "Choose type of info form available types: \n" \
            "movie\n" \
            "tv_series\n"

info_name = "Choose name of movie or tv_series\n"

info_continue = "Do you want to continue (y/n)? \n"

# variables
error = False


def main():
    working = True

    while working:
        type = input(info_type)
        print(type)
        name = input(info_name)
        print(name)

        # TODO obsluga zapytania i wszystkiego
        

        working = input(info_continue) == 'y'



if __name__ == "__main__":
    main()