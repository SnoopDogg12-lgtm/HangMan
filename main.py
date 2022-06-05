import requests
import json

#getting a random word from a random API
r = requests.get("https://random-words-api.vercel.app/word")
data = r.json()
data_word = data[0]['word']
print(data_word)

# defining some vars
word = data_word.lower()
answer = list(word)
word_lenght = len(word)
spaces = []
answer_list = []

# adding as many elements to the board as the lord lenght
for i in range(word_lenght):
    spaces.append("_")

print(*spaces)

#checking if the input is in the word
while len(answer_list) < word_lenght:
    user_input = str(input("Enter a letter: ")).lower()

    if user_input in word:

        letter_index = answer.index(user_input)

        #checking if the same letter occurs twice
        for letter_index in (idx for idx,l in enumerate(word) if l==user_input):
            spaces[letter_index] = user_input
            answer_list.append(user_input)

        print(*spaces)
    elif(user_input not in word):
        print("Letter is not in the word")
        print(*spaces)
    
