(''' LISTS:

1- Create a list of your favorite movies and print the third movie on the list .
2- Add a new movie to the end of the list and then remove the second movie.
3- Slice the list to create a new list containing the first three movie

 ''')

# fav movies
movies = ["ddlj", "kkkg","dilwale", "kkhh", "bajigar"]

# print 3rd movie
print(movies[2])

# add a new movie
movies.append("war")
print(movies)

# remove the second movie
remove = movies.pop(1)
print(movies)

# first 3 movie using slice
print(movies[0:3])
