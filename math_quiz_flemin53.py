"""
Author: Joseph Fleming, flemin53@purdue.edu
Assignment: m.n - Math Quiz
Date: 10/14/2021

Description:
    This program creates a function that accepts n as a parameter and returns a random number with n digits.
    Then, it asks the user to add 2 random numbers, 2 and 3 digits respetively.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

from random import *
def random_number(digits):
    return randint(10**(digits-1),(10**digits)-1) #A random number between the lowest correct digit number and the highest

def main():
    a = random_number(2) #must store the random values
    b = random_number(3) #necessary to check for correct answer
    print(f'   {a}')
    print(f'+ {b}')
    print('-----')
    answer = int(input('= ')) #Must be an integer to compare properly
    if answer == (a + b):
        print('Correct -- Good Work!')
    else:
        print(f'Incorrect. The correct answer is {a+b}.')


if __name__ == '__main__':
    main()
