
#If the resulting index number is 
# 16 or higher (equivalent to or greater than a senior undergraduate reading level), 
# your program should output “Grade 16+” instead of outputting an exact index number. 
# If the index number is less than 1, 
# your program should output “Before Grade 1”.

# L is the average number of letters per 100 words in the text: 
# that is, the number of letters divided by the number of words, 
# all multiplied by 100.

# S is the average number of sentences per 100 words in the text: 
# that is, the number of sentences divided by the number of words, 
# all multiplied by 100.

# Coleman-Liau index is computed using index = 0.0588 * L - 0.296 * S - 15.8

class Readability:
    def __init__(self, user):
        self.user = user
    
    def countGrade(self):
        #count letters
        letters = sum(1 for c in self.user if c.isalpha()) 
        
        #count sentence
        sentence = sum(1 for c in self.user if c in '.!?') 
        
        words = len(self.user.split())

        L = (letters / words) * 100
        S = (sentence / words) * 100

        #Coleman-Liau index
        index = 0.0588 * L - 0.296 * S - 15.8

        if index >= 16:
            print('Grade 16+')
        
        elif index < 1:
            print('Below Grade 1')
        
        else:
            print(f'Grade {round(index)}')




# Test 1
user = 'One fish. Two fish. Red fish. Blue fish'
out = Readability(user)
out.countGrade()

# Test 2
user1 = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."
out1 = Readability(user1)
print('User 1')
out1.countGrade()