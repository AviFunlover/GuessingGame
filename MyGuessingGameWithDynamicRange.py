#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
#using import random library

def checknum(guessnum):
    if guessnum>=a and guessnum<=b:
        return True
    else:
        return False
#using def function to create a small function to check if the number is within the range of the user defined range of random number
#and the checknum will return Boolean if the guessnum is within range
#True if in range || or false if out of range
    
    
a=int(input("Give the lower range of the number")) 
b=int(input("Give the upper range of the number"))
#creating variables a and b to store the value of the range, in the user whats to randomly generate a number
randnum=random.randint(a,b)
#randnum stores the randomly created value within the user-defined range in this (a,b) are inclusive

print(randnum)
#must be ommited. kept in the program for testing purpose only

guessnum=int(input(f"Give your Guess number between {a} and {b}.So Whats Your Guess? "))
#takes the guess number from the user and shows the range dynamically
d=guessnum-randnum
#stores the diffence of the guessed number and the random number
d=abs(d)
#overwrites it with its absolute value i.e., -7 becomes 7
x=[]
#initialisation of a list named x to store the difference
x.append(d)
#dynamically storing the absolute difference generated in d
i=0
#initialisation for index value storing
check=True
#initialisation of check to keep the boolean
check=checknum(guessnum)
#checks and stores the boolean if the guessnum is within range or not

if check==True:
#checks if the guessnum is within range if True, then passes it within for continuing
    if guessnum==randnum:
    #checks if the user has at once given the correct answer and congratulates him/her
        print("Congratulations You Guessed The Random Number Generated Correctly in One Go")
    else:
    #if the user was unable to give the correct answer at once then 
        if d<=10:
        #if the user's guessed number has a difference of less than or equal to 10 then it shows
            print("Warm! You are Very Close to The Number ")
        else:
        #if the user's guessed value has a difference of more than 10 then shows
            print("Cold! You will get there Try Again")
        
        while guessnum!=randnum:
        #will run untill the user has found the correct number
            guessnum=int(input("Give Another Guess: "))
            #again ask for new input
            check=checknum(guessnum)
            #checks if the new guessed number is within range
            if check==True:
            #if within range then enters to be compared
                d=guessnum-randnum
                #find the diffence of the new guessed number and the randnum
                d=abs(d)
                #overwrite its absolute value
                x.append(d)
                #dynamically append that number to the list
            
                if x[i+1]<x[i]:
                #checks if the diffence of the list's subsequent values are smaller. hence if the user is getting nearer to the randnum
                    print("Warmer! You are Getting Closer")
                    i=i+1
                else:
                #if user is getting further away
                    print("Colder! Ahh, You are getting away from the Number")
                    i=i+1
            else:
            #if guessed value is out of range
                print(f"OMMITTED!Your Guess is out of range. Try again! Give your guess between {a} and {b}.")
        print(f"Won atlast! After {len(x)} trials")

else:
#if the check is false then the game shows that the value is out of range and askes the user to restart the game
    print("Your First Guess is out of range. Restart! And Give Your Guess between the range you provided.")


# 

# In[ ]:





# In[ ]:




