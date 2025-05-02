'''
Hunt for the Wilderpeople Quiz
Aydrian Soukbandith-Yi
'''
import time

# MAKING A LIST FOR QUESTIONS
LIST_QUESTIONS = [
    'Who directed Hunt for the wilderpeople movie?\nA. Peter Jackson\nB. Taika Waititi\nC. Jane Campion\n',
    'Who played Ricky Baker?\nA. James Rolleston \nB. Teoreore Ngatai \nC. Julian Dennison\n',
    'Who played Uncle Hec?\nA. Sam Neil \nB. Hugh Jackman \nC. Russel Crowe \nD. Rhys Darby\n',
    'Aunt Bella died in Hunt for the wilderpeople?\nTrue?\nFalse?\n',
    'What crimes did Ricky Baker commit?\nA. Eating \nB. Crashing \nC. Stealing \nD. Robbery\n',
    'What year did Hunt for the wilderpeople come out?\nA. 2015 \nB. 2017 \nC. 2016 \nD. 2018\n' ]

LIST_ANSWERS = [
    'Taika Waititi',
    'Julian Dennison',
    'Sam Neil',
    'True',
    'Stealing',
    '2016' ]
    
points = 0  
    
print("Welcome to Hunt for the wilderpeople quiz!\nInstructions:\nTry to get 6 points by the end of this quiz\nThere will be 6 questions\nPlease type in answers, don't put in A,B,C..\n\n")
time.sleep(0.5)
    
for i in range (len(LIST_QUESTIONS)):
    print(f"{LIST_QUESTIONS[i]}")
    
    ans = input("Answer: ")
    ans = ans.lower().title()
    
    if ans == LIST_ANSWERS[i]:
        points +=1
        i =+1
        print(f"That's correct! You have {points} points!\n")
        time.sleep(0.5)
    else: 
       print(f"That's incorrect. The answer was: {LIST_ANSWERS[i]}\nYou still have {points} points.\n")
       time.sleep(0.5)
      
print("I hope you enjoyed the quiz ")
print("Quiz program was created by Aydrian Soukbandith-Yi ")
quit()
