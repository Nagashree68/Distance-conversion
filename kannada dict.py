kan_dictionary = {
    "there" : "alli",
    "here" : "illi",
    "one" : "onduu"
}
print(kan_dictionary)
user = input("please enter the english word to find the kannada version:")
print(kan_dictionary.get(user))
words = user.split("_")
print(words)
for every in words:
    print(kan_dictionary.get(every))