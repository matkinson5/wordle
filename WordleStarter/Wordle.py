# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS as words
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR

def wordle():
    def change_color(enteredWord, word):
        is_color_blind = gw.get_color_mode()
        square_colors, key_colors = set_color_squares(is_color_blind)

        rowNum = gw.get_current_row()
        word_dict = {}

        # Create a dictionary to count the occurrences of each letter in the target word
        for i in range(N_COLS):
            if word[i] in word_dict:
                word_dict[word[i]] += 1
            else:
                word_dict[word[i]] = 1

        for i in range(N_COLS):
            if enteredWord[i] == word[i]:
                square_color = square_colors["correct"]
            else:
                if enteredWord[i] in word_dict and word_dict[enteredWord[i]] > 0:
                    square_color = square_colors["present"]
                else:
                    square_color = square_colors["missing"]

            if is_color_blind:
                key_color = key_colors["correct"] if enteredWord[i] == word[i] else (
                    key_colors["present"] if enteredWord[i] in word_dict and word_dict[enteredWord[i]] > 0 else key_colors["missing"])
                key_color = "blue" if key_color == key_colors["correct"] else (
                    "orange" if key_color == key_colors["present"] else "red")
            else:
                key_color = key_colors["correct"] if enteredWord[i] == word[i] else (
                    key_colors["present"] if enteredWord[i] in word_dict and word_dict[enteredWord[i]] > 0 else key_colors["missing"])

            gw.set_square_color(rowNum, i, square_color)
            gw.set_key_color(enteredWord[i].upper(), key_color)

            # Decrement the count for the letter in the dictionary
            if enteredWord[i] == word[i]:
                word_dict[word[i]] -= 1

    def set_color_squares(is_color_blind):
        if is_color_blind:
            square_colors = {
                "correct": "blue",
                "present": "orange",
                "missing": "red",
                "unknown": UNKNOWN_COLOR,
            }
            key_colors = {
                "correct": "blue",
                "present": "orange",
                "missing": "red",
            }
        else:
            square_colors = {
                "correct": CORRECT_COLOR,
                "present": PRESENT_COLOR,
                "missing": MISSING_COLOR,
                "unknown": UNKNOWN_COLOR,
            }
            key_colors = {
                "correct": CORRECT_COLOR,
                "present": PRESENT_COLOR,
                "missing": MISSING_COLOR,
            }
        return square_colors, key_colors

    def check_correct_letters(enteredWord, word): #checks if the word is the selected random word
        if enteredWord == word:
            return True 
        else: 
            return False 

    def check_word(enteredWord): #checks if the word entered is in the word dictionary

        if enteredWord in words:
            return True
        else:
            return False
        
        

    # def choose_alternate_colors():
    #     while True:
    #         user_choice = input("Do you want to use the alternate color scheme? (yes/no): ").strip().lower()
    #         if user_choice == "yes":
    #             return True
    #         elif user_choice == "no":
    #             return False
    #         else:
    #             print("Invalid input. Please enter 'yes' or 'no'.") 

    def enter_action(s):
        enteredWord = s.lower()

        if check_word(enteredWord):
            won = check_correct_letters(enteredWord, word)
            # change_color(enteredWord, word, square_colors, key_colors, use_alternate_colors)
            change_color(enteredWord, word)
            currentRow = gw.get_current_row()

            if currentRow < 5 and not won:
                gw.set_current_row(currentRow + 1)
                message = "Keep going"
            elif won:
                message = "You won"
                gw.enable_button()

            else:
                message = "Try again tomorrow"

        else:
            message = "Not in the word list"

        gw.show_message(message)

    # I moved this code so that it worked with the button
    # Call the function from WordleGraphics.py to choose the color scheme
    # use_alternate_colors = choose_alternate_colors()

    # if use_alternate_colors:
    #     square_colors = {
    #         "correct": "blue",
    #         "present": "orange",
    #         "missing": "red",
    #         "unknown": UNKNOWN_COLOR,
    #     }
    #     key_colors = {
    #         "correct": "blue",
    #         "present": "orange",
    #         "missing": "red",
    #     }
    # else:
    #     square_colors = {
    #         "correct": CORRECT_COLOR,
    #         "present": PRESENT_COLOR,
    #         "missing": MISSING_COLOR,
    #         "unknown": UNKNOWN_COLOR,
    #     }
    #     key_colors = {
    #         "correct": CORRECT_COLOR,
    #         "present": PRESENT_COLOR,
    #         "missing": MISSING_COLOR,
    #     }

    gw = WordleGWindow()

    word = randomWord()

    gw.add_enter_listener(enter_action)

def randomWord():
    min_value = 1
    max_value = len(words)  # You can adjust the range as needed

    random_integer = random.randint(min_value, max_value)

    word = words[random_integer]

    # not necessarily needed but good for testing
    print(word)
    return word

# Startup code
if __name__ == "__main__":
    wordle()


