# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS as words
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR, KEY_COLOR

def wordle():
    def change_color(enteredWord, word):
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
                gw.set_square_color(rowNum, i, CORRECT_COLOR)
                gw.set_key_color(enteredWord[i].upper(), CORRECT_COLOR)
                # Decrement the count for the letter in the dictionary
                word_dict[word[i]] -= 1
        for i in range(N_COLS):
            if enteredWord[i] != word[i] and enteredWord[i] in word_dict and word_dict[enteredWord[i]] > 0:
                gw.set_square_color(rowNum, i, PRESENT_COLOR)
                if gw.get_key_color(enteredWord[i].upper()) != CORRECT_COLOR:
                    gw.set_key_color(enteredWord[i].upper(), PRESENT_COLOR)
                # Decrement the count for the letter in the dictionary
                word_dict[enteredWord[i]] -= 1
            elif gw.get_square_color(rowNum, i) != CORRECT_COLOR:
                gw.set_square_color(rowNum, i, MISSING_COLOR)
                if gw.get_key_color(enteredWord[i].upper()) != CORRECT_COLOR and gw.get_key_color(enteredWord[i].upper()) != PRESENT_COLOR:
                    gw.set_key_color(enteredWord[i].upper(), MISSING_COLOR)
        print(word_dict)

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
        
        

    def enter_action(s):
        
        enteredWord = s.lower()

        if check_word(enteredWord):
            won = check_correct_letters(enteredWord, word)
            print(word)
            change_color(enteredWord, word)
            currentRow = gw.get_current_row()

            if currentRow < 5 and won == False:
                gw.set_current_row(currentRow + 1) 
                message = currentRow
            elif won == True: 
                message= "You won"
            else:
                message = "Try again tomorrow"

        else:
            message = "Not in word list"


        gw.show_message(message)

    gw = WordleGWindow()

    word = randomWord()

    gw.add_enter_listener(enter_action)

def randomWord():
    min_value = 1
    max_value = len(words) # You can adjust the range as needed

    random_integer = random.randint(min_value, max_value)

    word = words[random_integer] 

    return word

# Startup code

if __name__ == "__main__":
    wordle()



