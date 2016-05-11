import random
from random import randrange
import string

questions = ["This Commander-in-Chief of the Continental Army later became the first President of the United States?", 
    		"This famous actor just won his first Oscar after 26 years of acting.", 
    		"A force that attracts a body toward the center of the earth?", 
    		"The name of this country, whose national animal is the beaver, comes from an Indian word that means Big Village?", 
    		"In this novel, Atticus Finch defends a black man under trial despite criticism from his neighbors in Maycomb county"]
    
answers = ["george washington", "leonardo dicaprio", "gravity", "canada", "to kill a mockingbird"]


def main():
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print ("Welcome to the Mystery Door!")
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	state = 0
	

	while (True):
		
		if state == 0:
			print ("You awaken in a room filled with mystery. Which way will you go?")
			command = input("Front or Back: ")
			if command == "Front" or command == "front":
				print ("You are going towards Mystery Door")
				state = 1
			elif command == "Back" or command == "back":
				print ("You are running away?")
				state = 6
			else:
				print ("Wrong input. Try Again")
				state = 0
		if state == 1:
			print ("You are in front of the Mystery Door. Will you open it?")
			command = input("Open or Close: ")
			if command == "Open" or command == "open":
				print ("Oh boy...mystery")
				state = 2
			elif command == "Close" or command == "close":
				print ("Come on man.....")
				state = 8
			else:
				print ("Wrong input. Try Again")
				state = 1
		elif state == 2 :
			print ("There's a sword on the floor. Do you pick it up?")
			command = input("Yes or No: ")
			if command == "Yes" or command == "yes":
				print ("Gained +5 attack but accidentally cut your pants +10 embarassment")
				state = 3
			elif command == "No" or command == "no":
				print ("Continue moving like a badass")
				state = 3
			else:
				print ("Wrong input. Try Again")
				state = 2 
				
		elif state == 3:
			random_item = random.choice(questions)
			correctAnswer = answerToQuestions(random_item)
			print ("You are now approaching Big Bandit...")
			command = input("Fight or Run: ")
			if command == "Fight" or command == "fight":
				print ("In order to defeat me you must answer my questions HAHAHAHA ")
				command = input("Answer or Nah: ")
				if command == "Answer" or command == "answer":
					randomQuestion2 = randomQuestion(random_item)
					print (randomQuestion2)
					userAnswer = input("Whats your answer: ")
					userAnswer = userAnswer.lower()
					checkAnswer2 = checkAnswer(userAnswer, correctAnswer)
					state = 4 
				elif command == "Nah" or command == "nah":
					print ("You're so close yet you lost")
					state = 8
				else:
					print ("Wrong input. Try Again")
					state = 3
			elif command == "Run" or command == "run":
				print ("I guess the mystery door was too much for you")
				state = 6
			else:
				print ("Wrong input. Try Again")
				state = 3

		
		
		elif state == 4:
			print("You are now approaching Brooky carvan... Do you want to continue? ")		
			command = input("Yes or No: ")
			if command == "Yes" or command == "yes":
				 
				removeQuestion = questions.remove(randomQuestion2)
				#print (questions)
				next_random_item = random.choice(questions)
				nextQuestion = randomQuestion(next_random_item)
				print (nextQuestion)
				
				
				removeAnswer = answers.remove(userAnswer)
				correctAnswer2 = answerToQuestions(next_random_item)
				next_userAnswer = input("Whats your answer: ")
				next_userAnswer = next_userAnswer.lower()
				checkAnswer3 = checkAnswer(next_userAnswer, correctAnswer2)
				state = 5
		else:
			print ("You're so close yet you lost")
			state = 8

		elif state == 5:
			print("You are now approaching moody carvan... Do you want to continue? ")		
			command = input("Yes or No: ")
			if command == "Yes" or command == "yes":
				 
				removeQuestion1 = questions.remove(nextQuestion)
				#print (questions)
				next_random_item1 = random.choice(questions)
				nextQuestion1 = randomQuestion(next_random_item1)
				print (nextQuestion1)
				
				removeAnswer1 = answers.remove(next_userAnswer)
				correctAnswer3 = answerToQuestions(next_random_item1)
				next_userAnswer1 = input("Whats your answer: ")
				next_userAnswer1 = next_userAnswer1.lower()
				checkAnswer4 = checkAnswer(next_userAnswer1, correctAnswer3)
				state = 6
				
		elif state == 6:
			print("You are now approaching brooksberk... Do you want to continue? ")		
			command = input("Yes or No: ")
			if command == "Yes" or command == "yes":
				 
				removeQuestion2 = questions.remove(nextQuestion1)
				next_random_item2 = random.choice(questions)
				nextQuestion2 = randomQuestion(next_random_item2)
				print (nextQuestion2)
				
				removeAnswer2 = answers.remove(next_userAnswer1)
				correctAnswer4 = answerToQuestions(next_random_item2)
				#print(correctAnswer4)
				next_userAnswer2 = input("Whats your answer: ")
				next_userAnswer2 = next_userAnswer2.lower()
				checkAnswer5 = checkAnswer(next_userAnswer2, correctAnswer4)
				state = 7
		
		elif state == 7:
			print("You are now approaching berk... Do you want to continue? ")		
			command = input("Yes or No: ")
			if command == "Yes" or command == "yes":
				 
				removeQuestion2 = questions.remove(nextQuestion2)
				next_random_item3 = random.choice(questions)
				nextQuestion3 = randomQuestion(next_random_item3)
				print (nextQuestion3)
				
				removeAnswer3 = answers.remove(next_userAnswer2)
				correctAnswer5 = answerToQuestions(next_random_item3)
				#print(correctAnswer4)
				next_userAnswer3 = input("Whats your answer: ")
				next_userAnswer3 = next_userAnswer3.lower()
				checkAnswer6 = checkAnswer(next_userAnswer3, correctAnswer5)
				state = 8
		
		elif state == 8:
			print("GAME OVER")
			print("THE END?: ")
			command = input("Y / N: ")
			if command =="N" or command == "n":
				state = 0
			else:
				print ("BYE")
				break

    
def randomQuestion(random_item1):
	#random_item1 = random.choice(questions)
	return random_item1

#def popMe():
	


def answerToQuestions(random_item2):    
    random_index = questions.index(random_item2)

    if random_index == 0:
        answer = answers[0]
    elif random_index == 1:
     	answer = answers[1]
    elif random_index == 2:
     	answer = answers[2]
    elif random_index == 3:
     	answer = answers[3]
    elif random_index == 4:
     	answer = answers[4]
    return answer

def checkAnswer(string1, string2):
	
	if string1 == string2:
		print ("Ahh I am defeated")
	else:
		print ("Wrong answer!")


main()