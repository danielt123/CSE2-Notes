import random
word_bank = ['shoes', "cheeseburgers", "edison", "daniel", "football", "fries", "money", "tacos", "polo", "chocolate"]
length = len(word_bank)
range(11)
range(len(word_bank))

randomWords = random.choice(word_bank)
Guesses_left = 10
letters_guessed = [' ']
user_input = ""
print("You have 10 guesses to win")
while Guesses_left > 0:
    output = []
    for letter in randomWords:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    print(Guesses_left)

    if output == list(randomWords):
        print("You win")


    user_input = input("Type in a letter: ")
    letters_guessed.append(user_input)
    print(letters_guessed)

    if user_input not in list(randomWords):
        print("Guess again")
        Guesses_left -= 1