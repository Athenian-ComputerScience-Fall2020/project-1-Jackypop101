# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://stackoverflow.com/questions/36550812/how-can-i-detect-multiple-words-from-a-string-python
import random
s1list = []

name = input("Hello! My name is Serena, what is your name?")
if name == 'Jack':
    print("Thats a great name, its just like the boy who once created me for his computer science project!")
else: 
    print("Hi " + name + " it is great meeting you!")

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
while True:
    try:
        number = int(input("Now let's play a game! Pick a number from 1-10 and I will tell if you are thinking of the same number as me."))
        xnum = random.randint(1,10)
        if number == xnum:
            print("Good job, I was think of " + str(xnum) + " too!")
            break
        else:
            print("Nope, keep guessing.")
    except:
        number = int(input("please enter a number from 1-10"))

game = input("would you like to play another math game with me?")
if game == 'yes':
    print("Great! now I want you to want you to find the sum of the number that I will randomly write!")
    sum1 = 0
    for x in range (1,11):
        sum1 = sum1 + x
        print(x)
        y = random.randint(1,11)
        if x == y:
            break
    Sum = int(input("what is the sum?"))
    if Sum == sum1:
        print("Good job that is the right answer.")



