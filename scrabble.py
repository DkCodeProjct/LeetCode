
##In the game of Scrabble, players create words to score points, 
# and the number of points is the sum of the point values 
# of each letter in the word.

##For example, if we wanted to score the word “CODE”, 
# we would note that the ‘C’ is worth 3 points, 
# the ‘O’ is worth 1 point, the ‘D’ is worth 2 points, 
# and the ‘E’ is worth 1 point. Summing these, 
# we get that “CODE” is worth 7 points.




scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}


def countSocres(answr1, answr2):
    val1 = 0
    val2 = 0

    for char1, char2 in zip(answr1.upper(), answr2.upper()):
        if char1 in scores:
            val1 += scores[char1]
        
        if char2 in scores:
            val2 += scores[char2]
            
    return 'Tie.!' if val1==val2 else 'Player 1 Wins!' if val1>val2 else 'Player 2 Wins!'


user1 = input('Player 1: ')
user2 = input('Player 2: ')

print(countSocres(user1, user2))