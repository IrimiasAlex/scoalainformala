import random

from Hangman_words_list import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from Hangman_stages import logo
print(logo)

print(f'The solution is {chosen_word}.')

display = []
for letter in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word :
      print(f"You guessed {guess}, that is not in the word. You lose a life." )
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("YOU LOSE")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from Hangman_stages import stages
    print(stages[lives])