import random
randNumber= random.randint(1,100)
# print(randNumber) #hum randNumber print nhi karenge kyunke cheating hojayegi

userGuess= None #loop enter hone keliye iska defined hona zaroori h 
guesses= 0
while(randNumber!=userGuess):
    userGuess=int(input("Enter your guess: "))
    guesses+=1
    if (userGuess==randNumber):
        print("Your guess is correct")
    elif (userGuess<randNumber):
        print("higher number please...")
    else:
        print("lower number please...")

print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt","r") as f:
    hs=f.read()
print(hs)

if int(hs)>guesses:
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))
    print("Congratulations...You broke the hiscore")
    print(f"New hiscore is {str(guesses)}")