# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://stackoverflow.com/questions/36550812/how-can-i-detect-multiple-words-from-a-string-python
#megan
import random
s1list = []
#cup function
def function1():
    times = 0
    while True:
        try:
            print("\_1_/" , "\_2_/" , "\_3_/")
            cup1 = input("What cup is the ball in?")
            cupx = random.randint(1,3)
            if cup1 == 'quit':
                print("It's ok to give up sometimes, this is a very hard game! I hope you can come back and try it again.")
                break
            if int(cup1) == cupx:
                times = times + 1
                print("Great job you guesed it! ")
            elif int(cup1) != cupx:
                times = times - 1
                print("You got the wrong one, try again!")
            elif times == 3:
                print("Let's go! you got it right 3 times in a row. I knew you could do it! It is sad to see you go, but have a great day and make sure to visit me again!")
                break
        except:
            print("...")

#Countdown Function
def function_count():
    listcount = [5,4,3,2,1,"GO!"]
    for a in listcount:
        print(a)

#Introduction
name = input("Hello! My name is Jotaro, what is your name?")
if name == 'Jack':
    print("Thats a great name, its just like the boy who once created me for his computer science project!")
else: 
    print("Hi " + name + " it is great meeting you!")

#Responding feelings
while True:
    s1 = input("How are you today?")
    s1list.append(s1)
    s1list = s1.split()
    print(s1list)
    if 'sad' in s1list or "unhappy" in s1list or "depressed" in s1list:
        print( "Sadness will pass. It takes more muscles to frown than to smile, be HAPPY!" )
        break
    elif 'happy' in s1list or "great" in s1list or "good" in s1list:
        print("It great to hear that you are doing well! Keep it up and enjoy life!")
        break
    elif 'tired' in s1list or "lazy" in s1list or "sleepy" in s1list:
        print("It is ok to rest but make sure you are not wasting your valuebal time!")
        break
    elif 'angry' in s1list or "mad" in s1list:
        print("Anger will pass, take a deep breath and think about all your happy memories and things you are looking forward to.")
        break
    else:
        print("I am so sorry, my creator created me with limited vocabulary, please enter a simpler emotion:")
#random number game
xnum = random.randint(1,9)
print("Now let's play a game!")
while True:
    function_count()
    try:
        number = int(input("Pick a number from 1-10 and I will tell if you are thinking of the same number as me."))
        if number == xnum:
            print("Good job, I was think of " + str(xnum) + " too!")
            break
        else:
            print("Nope, keep guessing.")
    except:
        print("...")

#Factorials
game = input("would you like to play another math game with me?")
if game == 'yes':
    print("Great! now I want you to want you to find the sum of the number that I will randomly write.")
    function_count()
    sum1 = 0
    y = random.randint(1,11)
    for x in range (y):
        sum1 = sum1 + x
        print(x)
    Sum = int(input("what is the sum?"))
    if Sum == sum1:
        print("Good job that is the right answer.")
    else:
        print("No, you got it wrong. Its ok, games are only for fun :)")
if game =="no":
    print("It does not matter, you are going to play the game anyways. I want you to want you to find the sum of the number that I will randomly write!")
    function_count()
    sum1 = 0
    y = random.randint(1,11)
    for x in range (y):
        sum1 = sum1 + x
        print(x)
    Sum = int(input("what is the sum?"))
    if Sum == sum1:
        print("Good job that is the right answer.")
    else:
        print("No, you got it wrong. Its ok, games are only for fun :)")

#Cup game
print("Alright. I know that you are very busy, I have one last game for you!")
print("I have put a ball in on of the cups, you have to guess it right 3 times in a row to finish the game. If you want to quit, just enter quit. Good luck!")
function_count()
function1()

    