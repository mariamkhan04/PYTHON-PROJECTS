import random #random will genrate numbers 1,2,3 randomly which will be comp choice
#rock,paper or scissor game
def gameWin(comp,win):
    # if two values are equal declare a tie 
    if comp==you:
        return None
        # checking all possibilities if computer chose rock(r)
    elif comp=='r':
        if you=='s':
            return False
        else:
            return True
        # checking all possibilities if computer chose paper(p)
    elif comp=='p':
        if you=='r':
            return False
        else:
            return True
         # checking all possibilities if computer chose scissor(s)   
    elif comp=='s':
        if you=='p':
            return False
        else:
            return True

print("comp turn: Rock(r) Paper(p) or Scissor(s)?")
randNo =random.randint(1,3) #randint 1,2,3 m se ek num chose krke dedega and random--random nos genrate krta h and random.randint() ek built in module h
if randNo==1:
    comp = 'r'
elif randNo==2:
    comp = 'p'
else:
    comp = 's'

you=input("your turn: Rock(r) Paper(p) or Scissor(s)?")
a =gameWin(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("The game is tie!")
elif a:
    print("You win!")
else:
    print("you lose!")