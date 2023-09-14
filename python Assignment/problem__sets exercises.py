(''' SETS -

1- Create a set of programming language you know and add a new language.
2- Remove  a language from the set and then check if PYTHON is in set.
3- Create second set of language and find the interaction of the two set
''')

# create a set
language = {"c++", "python", "html", "css", "javascript"}

# add a new language
language.add("c")
print(language)

# Remove a language
language.remove("css")
print(language)

# check python
print(" python is available or not : ", "python" in language)

# new set
language2 = {"javascript", "bootstrap", "c++"}

# intersection
result = language . intersection(language2)
print(result)
