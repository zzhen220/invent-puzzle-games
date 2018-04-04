import random
HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
=========''', '''

 +---+
 |   |
 0   |
     |
     |
     |
=========''', '''

 +---+
 |   |
 0   |
 |   |
     |
     |
=========''', '''

 +---+
 |   |
 0   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 0   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 0   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=========''','''
 +---+
 |   |
[0   |
/|\  |
/ \  |
     |
=========''','''
 +---+
 |   |
[0]  |
/|\  |
/ \  |
     |
=========''']
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals':'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mule newt otter owl panda parrot pigeon python rabbit ram rat raven rgino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordList):
    # This function returns a random string from the passed dictionary of lists of strings, and the key also.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end = '')
    for letter in missedLetters:
        print(letter, end = '')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end = '')
    print()

def getSet(wordDict):
    #This function returns the key of the list of strings chosen by the player.
    print('Which set of words do you want to guess?')
    
    for k in wordDict:
        print(k, end = '')
    print()

    while True:
        print('Please enter a word.')
        secretKey = input()
        if secretKey in wordDict:
            return secretKey
        else:
            print('Please choose one from the words mentioned ABOVE')
    

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretKey = getSet(words)
secretWord = getRandomWord(words[secretKey])
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' corrct guesses, the word was "' + secretWord + '"' )
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretKey = getRandomWord(words)
        else:
            break
