import random
from os import system, name
from time import sleep 
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    clear()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 9
    print("Nu spelar vi Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Gissa en bokstav eller ett ord: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'Du har redan gissat på bokstaven {guess}')
            elif guess not in word:
                print(f'Bokstaven {guess} finns inte i ordet.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'Bra gissat {guess} finns i ordet!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'Du har redan gissat på den här bokstaven {guess}')
            elif guess != word:
                print(f'{guess} är fel ord.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Ogiltigt tecken.')
        
        sleep(2)
        clear()
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
        printGuessedWord(guessed_letters)
    if guessed:
        print('Grattis du har listat ut ordet! Du klarade det!')
    else:
        print(f'Tyvärr, du har inga fler gissningar kvar. Ordet var {word}. Kanske du lyckas nästa gång!')


def display_hangman(tries):
    stages = [  # 0.
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                |-----|
                """,
                # 1.
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                |-----|
                """,
                #2. 
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                |-----|
                """,
                # 3.
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                |-----|
                """,
                # 4.
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                |-----|
                """,
                # 5.
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                |-----|
                """,
                # 6.
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                |-----|
                """,
                # 7.
                """
                   --------
                   |      
                   |
                   |
                   |
                   |
                |-----|
                """,
                # 8.
                """
                   
                   |      
                   |
                   |
                   |
                   |
                |-----|
                """,
                # 9.
                """
                   
                         
                   
                   
                   
                   
                |-----|
                """
    ]
    return stages[tries]

def printGuessedWord(guessed_letters):
    print(f'Gissade bokstäver: {guessed_letters}\n')

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def main():
    word = get_word()
    play(word)
    while input("Vill du spela igen? (J/N) ").upper() == "J":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
