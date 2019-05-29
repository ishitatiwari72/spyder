# -*- coding: utf-8 -*-
"""
Created on Wed May  8 06:09:21 2019

@author: HP
"""
"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""





import random 
#print (random.__file__)    loc of file
r1 = random.randint(0,10)
print (r1)
r2 = int (input("enter the number"))
print (r2)
if r1 == r2:
    print ("player win")
    
else:
    print("computer wins")





"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""

print("secret number > {},guess number > {}".format(r1,r2))




"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""


if( r2 <= r1-2 and r2 >= r1+2 ):
    print("your guess is too low")
elif (r2 == (r1-1) and r2 == (r1+1)):
        print("your guess is too high")
else:
            print("your guess is correct")

"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""
i=1
while ( i == 1 ) :
    r2 =int( input("enter the number"))
    print (r2)
    if r1 == r2:
        print ("player win")
        i=0;
    else:
        print("computer win try again")
        




"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""

i=1
j=1
k=0
while ( i == 1 and j <= 6 ) :
    r3 =int( input("enter the number"))
    if r1 == r3:
        print ("player win")
        i=0
    else:
        print("computer win try again")
        j=j+1
        i=1
        k=k+6-j
        
        
"""
Challenge 6
    Print the number of tries left 
"""

print("remaining tries {}".format(k))


"""
Challenge 7
    Lets give user the option to play again
"""

print("play again")
i=1
j=1
while ( i == 1 and j <= 6 ) :
    r3 = int(input("enter the number"))
    if r1 != r3:
         print("computer win try again")
         j=j+1
         k=6-j
    else:
         print ("player win")
         i=0
         k=6-j

"""
Challenge 8
    Catch when someone submits a non integer
"""


print(isinstance(25,int))  # or isinstance(25,str))


""""try:
    n = raw_input("enter the value")
except ValueError:

"""
"""