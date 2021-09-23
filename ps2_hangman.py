# Problem set 2
# Name: Vaishnavi Mittal
# Time spent:3:00:00


import random

WORDLIST_FILENAME = "D:\PythonProblemSolvingCodeSumission\ps2\words.txt"

def loadWords():
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    
    return random.choice(wordlist)

# -----------------------------------
wordlist = loadWords()

def word_guessed(rand_word, letter_guessed):
    
    c=0
    for i in letter_guessed:
        if i in rand_word:
            c+=1
    if c==len(rand_word):
        return True
    else:
        return False


def getGuessedWord(rand_word, letter_guessed):
    
    s=[]
    for i in rand_word:
        if i in letter_guessed:
            s.append(i)
    answer=''
    for i in rand_word:
        if i in s:
            answer+=i
        else:
            answer+='_ '
    return answer



def available_letters(letter_guessed):
    
    import string
    ans=list(string.ascii_lowercase)
    for i in letter_guessed:
        ans.remove(i)
    return ''.join(ans)

def hangman(rand_word):


    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(rand_word),"letters long.")
    
    global letter_guessed
    mistake=0
    letter_guessed=[]
    
    while 8 - mistake > 0:
        
        if word_guessed(rand_word, letter_guessed):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            print("You have",8-mistake,"guesses left.")
            print("Available letters:",available_letters(letter_guessed))
            guess=str(input("Please guess a letter: ")).lower()
            
            if guess in letter_guessed:
                print("Oops! You've already guessed that letter:",getGuessedWord(rand_word,letter_guessed))
                
            elif guess in rand_word and guess not in letter_guessed:
                letter_guessed.append(guess)
                print("Good guess:",getGuessedWord(rand_word,letter_guessed))
                
            else:
                letter_guessed.append(guess)
                mistake += 1
                print("Oops! That letter is not in my word:",getGuessedWord(rand_word,letter_guessed))
                
        if 8 - mistake == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",rand_word)
            break
        
        else:
            continue


rand_word= chooseWord(wordlist).lower()
hangman(rand_word)
