print('Welcome to DarxPython Riddles')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?')
    if answer.lower()=='echo':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: What has keys but cannot open locks? ')
    if answer.lower()=='piano':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What can travel around the world while staying in a corner?')
    if answer.lower()=='stamp':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small riddle game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')