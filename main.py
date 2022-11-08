import random
from words import words
from hangman_display import parts


picked = random.choice(words) #choose random word
print('The word has', len(picked), 'letter')

right = ['_'] * len(picked)
wrong = []

#print number of'_'
def update():
    for i in right:
        print(i, end='')

update()
parts(len(wrong))

while True:
    print('\n==========================')
    guess = input('Guess a letter: ')

#thay '_' thanh tu da doan
    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index += 1
        update()

    else:
        if guess not in wrong:
            wrong.append(guess)
            print("Wrong, try again")
            parts(len(wrong))
        else:
            print("You already guessed that letter")
    if len(wrong) == 10:
        print('You lose!')
        print('The correct answer is: ', picked)
    if '_' not in right:
        print('\nYou win!')
        break