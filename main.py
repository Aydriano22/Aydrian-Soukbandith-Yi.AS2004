
# MAKING A LIST FOR QUESTIONS
question = ["Who directed Hunt for the wilderpeople movie? "
              "Who played Ricky Baker? "
               "Who played Uncle Hec? "
              "Did Aunt Bella die in Hunt for the wilderpeople? "
              "What crimes did Ricky Baker commit? "
              "What year did Hunt for the wilderpeople come out? "]


# Title
print("Welcome to Hunt for the wilderpeople quiz! ")
print('Instructions ')
print("Try to get 10 points by the end of this quiz ")
print("There'll be 6 questions ")
print("Please type in the answers, don't put in A,B,C.. ")

points = 0


print(list_questions1[0])

print()
answer = input("\n A. Peter Jackson \n B. Taika Waititi \n C. Jane Campion \n Answer: ").lower()

if answer == 'taika waititi':
    print("That's correct, Taika Waititi also directed other movies, such as Thor love & Thunder ")
    points += 1
else: 
    print("That's incorrect, good try ")
    print("The correct answer was Taika Waititi ")
    



print(list_questions2[0])

print()
answer = input("\n A. James Rolleston \n B. Teoreore Ngatai \n C. Julian Dennison \n Answer: ").lower()


if answer == 'julian dennison':
    print("That's correct, you're onto it ")
    points += 1
else:
    print("That's incorrect ")
    print("The correct answer was Julian Dennison ")



print(list_questions3[0])

print()
answer = input("\n A. Sam Neil \n B. Hugh Jackman \n C. Russel Crowe \n D. Rhys Darby \n Answer: ").lower()

if answer == 'sam neil':
    print("That's correct, did you know Sam Neil was in the Jurrasic Park movie ")
    points += 2
else: 
    print("That's incorrect ")
    print("The correct answer was Sam Neil ")
    


print(list_questions4[0])

print()
answer = input('True? or False? ').lower()

if answer =='true':
    print("That's correct, Great job! ")
    points += 2
else:
    print("That's incorrect ")
    


print(list_questions5[0])

print()
answer = input("\n A. Eating \n B. Crashing \n C. Stealing \n D. Robbery \n Answer: ").lower()

if answer == "stealing":
    print("That's correct, Nice! ")
    points += 3
else:
    print("That's incorrect ")
    print("The correct answer was stealing ")


print(list_questions6[0])

print()

answer = input("\n A. 2015 \n B. 2017 \n C. 2016 \n D. 2018 \n Answer: ").lower()


if answer == '2016':
    print("That's correct ")
    print("You are superior! ")
    points +=1
else:
    print("That's incorrect, the correct answer was '2016' ")
    print("Try again next time ")


print("Your results " + str(points) + "points correct!")
print("I hope you enjoyed the quiz ")


print("Quiz program was created by Aydrian Soukbandith-Yi ")
print()
answer = input("\n A. James Rolleston \n B. Teoreore Ngatai \n C. Julian Dennison \n Answer: ").lower()


if answer == 'julian dennison':
    print("That's correct, you're onto it ")
    points += 1
else:
    print("That's incorrect ")
    print("The correct answer was Julian Dennison ")



print(list_questions3[0])

print()
answer = input("\n A. Sam Neil \n B. Hugh Jackman \n C. Russel Crowe \n D. Rhys Darby \n Answer: ").lower()

if answer == 'sam neil':
    print("That's correct, did you know Sam Neil was in the Jurrasic Park movie ")
    points += 2
else: 
    print("That's incorrect ")
    print("The correct answer was Sam Neil ")
    


print(list_questions4[0])

print()
answer = input('True? or False? ').lower()

if answer =='true':
    print("That's correct, Great job! ")
    points += 2
else:
    print("That's incorrect ")
    


print(list_questions5[0])

print()
answer = input("\n A. Eating \n B. Crashing \n C. Stealing \n D. Robbery \n Answer: ").lower()

if answer == "stealing":
    print("That's correct, Nice! ")
    points += 3
else:
    print("That's incorrect ")
    print("The correct answer was stealing ")


print(list_questions6[0])

print()

answer = input("\n A. 2015 \n B. 2017 \n C. 2016 \n D. 2018 \n Answer: ").lower()


if answer == '2016':
    print("That's correct ")
    print("You are superior! ")
    points +=1
else:
    print("That's incorrect, the correct answer was '2016' ")
    print("Try again next time ")


print("Your results " + str(points) + "points correct!")
print("I hope you enjoyed the quiz ")


print("Quiz program was created by Aydrian Soukbandith-Yi ")
