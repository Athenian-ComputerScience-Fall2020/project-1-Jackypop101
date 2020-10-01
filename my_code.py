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
    s1list = s1.split()
    if "sad" or "depressed" or "bad" in s1list:
        print( "Sadness will pass. It takes more muscles to frown than to smile, be HAPPY!" )
        break
    elif 'happy' or 'great' or "awesome" or "amazing"  in s1list:
        print("It great to hear that you are doing well! Keep it up and enjoy life!")
        break
    elif 'tired' or 'bored' or 'lazy' in s1list:
        print("It is ok to rest but make sure you are not wasting your valuebal time!")
        break
    elif 'angry' or 'pissed' or 'mad'in s1list:
        print("Anger will pass, take a deep breath and think about all your happy memories and things you are looking forward to.")
        break    
    else:
        print("I am so sorry, my creator created me with limited vocabulary, please enter a simpler emotion:")




