import random 
from words import words
import string

def valid_words(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word= random.choice(words)
    
    return word.upper()

def hangman():
    word = valid_words(words)
    letters = set(word) #letters in the word file
    alphabets= set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    
    lives = 6
    
    #getting user input
    while len(letters) > 0 and lives > 0:
        #letters used
        print('You have',lives,' lives left and You have used these letters: ', ' '.join(used_letters)) 
        
        #what the current word is (i.e W- R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)
                
            else:
                lives = lives - 1
                print('Letter is not in the word')
        
        elif user_letter in used_letters:
            print('Letter has been used, please try again')
        
        else:
            print('Invalid letter, please try again')  
                  
    if lives == 0:
        print('you died the word was', word)
    else :
        print('Yay! you guessed the word', word, 'correctly')
        
hangman()
    