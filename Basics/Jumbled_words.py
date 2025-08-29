import random

def choose_random_word(word_list):
    return random.choice(word_list)

def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

def main():
    word_list = ["scientist", "whatsapp", "announcement", "hostelites", "phone", "strawberry","school","python","refrigerator","college","instagram","facebook"]

    print("Welcome to the Jumble Word Game!")
    print("Unscramble the letters to make a word.")

    while True:
        chosen_word = choose_random_word(word_list)
        jumbled = jumble_word(chosen_word)

        print("Jumbled word:", jumbled)
        guess = input("Your guess: ").strip().lower()

        if guess == chosen_word:
            print("Congratulations! You guessed the word correctly!")
        else:
            print("Sorry, that's not correct. Try again.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()