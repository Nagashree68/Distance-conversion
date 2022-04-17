#counting the number of words ....word counter

text_variable = "Microdegree is a learning platform. I learn programming at Microdegree"

count = 0
word_list = text_variable.split(" ")
print(word_list)

for every_word in word_list:
    if("Microdegree"==every_word):
        count = count +1

print(count)