import random

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to the Mystery Door!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

lifeBar = 3

state = 0

random_item = []
global questions 
#answers = ["George Washington", "Leonardo DiCaprio", "gravity", "Canada", "To Kill A Mockingbird"]
global storage

#def checkLife(): 
 #   global lifeBar
    #print("Your current life is: " + str(lifeBar))
    #if(lifeBar == 0):
       # state = 2
    
def question():
    #questions = ["This Commander-in-Chief of the Continental Army later became the first President of the United States?", "This famous actor just won his first Oscar after 26 years of acting.", "A force that attracts a body toward the center of the earth?", "The name of this country, whose national animal is the beaver, comes from an Indian word that means Big Village?", "In this novel, Atticus Finch defends a black man under trial despite criticism from his neighbors in Maycomb county"]
    QA = [
        
        ["This Commander-in-Chief of the Continental Army later became the first President of the United States?","George Washington"],["This famous actor just won his first Oscar after 26 years of acting.","Leonardo DiCaprio"],["A force that attracts a body toward the center of the earth?","gravity"],["The name of this country, whose national animal is the beaver, comes from an Indian word that means Big Village?", "Canada"],["In this novel, Atticus Finch defends a black man under trial despite criticism from his neighbors in Maycomb county","To Kill A Mockingbird"]]
    global random_item 
    random_item = random.choice(QA)
    #current_item = random_item
    #random_item.pop(current_item)
    #stash = [item for item in questions if item not in storage]
    #ran = random.choice(stash)
    #for index in range(len(questions)):
       # print('current question :', questions[index])
        #if(random_item == questions[index]):
           # random_item = random.choice(questions)        
    print(random_item[0])

while(True):
    #question()
    if(state == 0):
        print("You awaken in a room filled with mystery. Which way will you go?")
        command = input("Front or Back: ")
        if(command == "Front"):
            print("you are going towards Mystery Door")
            state = 1
        elif(command == "Back"):
            print("you are running away?")
            state = 6
        else:
            print("Wrong input")
            state = 0
    if(state == 1):
        print("You are in front of the Mystery Door. Will you open it?")
        command = input("Open or Close: ")
        if(command == "Open"):
            print("Oh boy...mystery")
            state = 2
        elif(command == "Close"):
            print("Come on man.....")
            state = 6
        else:
            print("Wrong input")
            state = 1
    if(state == 2):
        print("There's a sword on the floor. Do you pick it up?")
        command = input("Yes or No: ")
        if(command == "Yes"):
            print("Gained +5 attack but accidentally cut your pants +10 embarassment")
            state = 3
        elif(command == "No"):
            print("Continue moving like a badass")
            state = 3
        else:
            print("Wrong input")
            state = 2 
    if(state == 3):
        print("You are now approaching Big Bandit...")
        command = input("Fight or Run: ")
        if(command == "Fight"):
            print("In order to defeat me you must answer my questions HAHAHAHA ")
            command = input("Answer or Nah: ")
            print(question())
            command = input("Whats your answer: ")
            if(command == random_item[1]):
                print("ahh I am defeated")
                state = 6
            else:
                    print("wrong!")
                    state = 6
        #elif(command == "Run"):
            #print("I guess the mystery door was too much for you")
            #state = 6
    #if(state == 4):
      #  print("You are approaching Giant Frog man... He is ready to redeem Big Bandit")
   
        #if(command == "Fight"):
           # print(question())
        
        #if(command == random_item[1]):
            #print("My master will avenge me")
 
           # print("I knew you were a loser!!")
            #state = 6
    #if(state == 5):
       # Print("You are approaching ULTRA BIG BOSS LAST FIGHT!@!!@@!")
        #command = input("Fight or Cry")
        #if(command == "Fight"):
            #print(question())
            #print("AHHHHHH you win")
        #else:
           # state =6  
    if(state == 6):
            print("GAME OVER")
            print("THE END?: ")
            command = input("Y/N: ")
            if(command =="N"):
                state = 0
            else:
                break
         