# Movie and music rater

For movie or tv series user gives title of the show and gets information about popularity, voice count, average rating
etc. In case of music, user gives artist name and program shows us the most popular artist which are similar to given
one and the most popular songs by this artist.

Main goal of program is to give user information so that the user can decide if movie or artist is worth the attention.

Movie worth watching factor: f = (popularity * vote_count)/(10 - vote_avg)
Music involvement factor: f = views / listeners

If movie worth factor is higher it is more probable to be good.
If music involvement factor is higher it means more there are more views per listener so listeners are more involved so
it is more probable that music is good.
