#Problem Set 3b
#Name: Vaishnavi Mittal
#Time spent: 1 day
#Comment:I tried doing ps3b as much as I could, unfortunately I got stuck with these functions.
from ps3a import *
import time
from perm import *

#
#
# Problem #6A: Computer chooses a word
#
#

def comp_get_valid_words_with_scores(hand, word_list):
    """
    Given a hand and a word_list, returns a list of valid words
        sorted in descending order according to their word scores
    
    return list ( tuple (int,string) ) sorted according to int,
        or None if no valid words are found

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_list, find a valid word, and return it.
    This word should be calculated by considering all possible permutations
    of lengths 1 to hand length.
    
    Hint: First try to make a legal player, and then worry about making
    the computer player better (if you have time). 

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO...
    
#
# Problem #6C: Playing a game
#
#

def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    letters=['n','r','e']
    hand=None
    
    while letters=='':
        print("Enter a command(n,r or e):\n")
        command=input()
        if command=="n":
            hand=deal_hand(HAND_SIZE)
        elif command=="r":
            if hand== None:
                print("You can play your last hand!")
                continue
        else:
            return

        print("is computer playing or user?")
        player=input()
        if player=='c':
            comp_play_hand(hand,word_list,HAND_SIZE)
        elif player=='u':
            play_hand(hand,word_list,HAND_SIZE)

    # TO DO...

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
