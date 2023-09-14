(''' DICTIONARY -

1- Create a dictionary of book title and their author
2- Add new book to the dictionary and then update the author of an existing book
3- Loop through the dictionary and print each book title and author

''')

books = {
    "The boy who loved" : "Durjoy Dutta",
    "Wuthering Heights" : "Emily Brontë",
    "The great gatsby" : "F.  Fitzgerald",
    "One indian Girl" : "Chetan Bhagat"
}

# adding a new book
books ["Hold my hand"] : "Durjoy Dutta"
print(books)

# update
books["Wuthering Heights"] = "F. Scott Fitzgerald"

# looping
print("book and authors : ")
for key,value in books.items():
    print(key, " : ", value)
