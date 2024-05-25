# Imports 
import random


# define the game

class WordGuessle:
    """Runs the logic of the game.
        Args:
        wordlist, max guesses
        Methods:
        read_word_list, generate_answer, get_guess, check_guess, is_won, is_lost, show_guess_history, play
    """
    def __init__(self, wordlist, max_guesses=6):
        self.wordlist = wordlist
        self.answer = self.generate_answer()
        self.guesses = [] # starts empty
        self.max_guesses = max_guesses # default is 6

    def read_word_list(filename):
        """Reads a text file containing a list of words.
        Args: filename: the path to the text file.
        Returns: a list of the words"""
        words = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    word = line.strip()
                    if len(word) == 5:
                        words.append(word.lower())
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except PermissionError:
            print(f"Error: Permission denied while reading ''{filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return words
    
    def generate_answer(self):
        """ Selects a single word from the list from read_word_list """
        return random.choice(self.wordlist)
    
    def get_guess(self):
        """ Gets user input and returns it as all lower-case """
        guess = input("Please guess a five-letter word: ")
        return guess.lower()
    
    def check_guess(self, guess):
        """ Checks answer for each letter, and creates a feedback list informing player of """
        feedback = []
        for i in range(5):
            if guess[i] == self.answer[i]:
                feedback.append('*') # correct letter in correct position
            elif guess[i] in self.answer:
                feedback.append('+') # correct letter, incorrect position
            else:
                feedback.append('X') # letter not in answer
        return feedback
    
    def is_won(self):
        for guess in self.guesses:
            if guess == self.answer:
                return True
        return False 
    
    def is_lost(self):
        return len(self.guesses) == self.max_guesses
    
    def show_guess_history(self, guesses, feedback):
      """ Creates two lists of previous guesses and feedbacks and prints them """
        guess_letters_list = []
        guess_feedback_list = []
        for guess in guesses:
            guess_letters = []
            guess_feedback = []
            guess_letters.extend(list(guess))
            guess_feedback.extend(self.check_guess(guess))
            guess_letters_list.append(guess_letters)
            guess_feedback_list.append(guess_feedback)
        for i in range(len(guesses)):
            print(guess_letters_list[i])
            print(guess_feedback_list[i])
                
    def play(self):
        """ Main method of the program which calls all other functions """
        print("""Welcome to Word Guessle! A random five-letter word has been selected. 
        Please guess up to six five-letter words. """)
        while not self.is_won() and not self.is_lost():
            guess = self.get_guess()
            self.guesses.append(guess)
            feedback = self.check_guess(guess)
            self.show_guess_history(self.guesses, feedback)
            print("""
            A '*' means the letter is in the correct place. 
            A '+' means the letter is in the word but in the incorrect place.
            A 'X' means the letter is not in the word.
            """)
        if self.is_won():
            print("Congratulations, you won!")
        else:
            print(f"You lost! The word was {self.answer}.")

# main driver of the program
wordlist = WordGuessle.read_word_list("words.txt")  # can be updated with a different dictionary of words-- just change the name of the txt file
game = WordGuessle(wordlist) # creates an object WordGuessle with the wordlist created above
game.play() # starts one round of the game
