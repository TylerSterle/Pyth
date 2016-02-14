'''
Created on Feb 13, 2016

@author: tyler_000
'''

if __name__ == '__main__':
    pass

import random #Function for picking a random answer from the ball.
import sys #Function that allows the user to terminate the program.


name = raw_input('Who am I speaking to? ') 
print ('Hello ' + name + '! ') #Ball will greet the user after user inserts name.

#List containing all of the possible answers from the ball.
possible_answers = ["It is certain ",
                    "It is decidedly so ",
                    "Without a doubt ",
                    "Yes, definitely ",
                    "You may rely on it ",
                    "As I see it, yes ",
                    "Most likely ",
                    "Outlook good ",
                    "Yes ",
                    "Signs point to yes ",
                    "Reply hazy try again ",
                    "Ask again later ",
                    "Better not tell you know ",
                    "Cannot predict now ",
                    "Concentrate and ask again ",
                    "Don't count on it ",
                    "My reply is no ",
                    "My sources say no ",
                    "Outlook not so good ",
                    "Very doubtful "]

#Function for the ball prompting the user to ask a question.
question = raw_input('Press the "enter" key and type your question below.  ')

while (raw_input(question) != "exit"):
    print (random.choice(possible_answers))
else:
    sys.exit('Goodbye')

"""
If the user types in any question as the input, the program will
print a random answer from the list, "possible_answers".
The program will terminate if the user's input is "exit"
where the ball with print a closing statement, "Goodbye".
"""
