import random
print("WELCOM TO NUMBER GUESSERS")
with open("score.txt") as sc:
    content = int(sc.read())
    print("High Score is",content)
x=int(input("How many rounds do you wanna play? : "))
y=x
points=0
while(x>0):
    print("*******************")
    print("ROUND ",y-x+1)
    print("*******************")
    number=int(random.randint(0,10))
    x-=1
    g=5
    while g>0:
        guess=int((input("Enter Your Number: ")))
        if(guess>number): 
            print("ATTEMPTS LEFT: ",g)
            print("(too big)")
        elif(guess<number ): 
            print("ATTEMPTS LEFT: ",g)
            print("(too small)")
        else:
            points+=1
            print("!!!!!!CONGRATS!!!!!") 
            break
        g-=1
if(points>content): print("*********NEW HIGH SCORE*******")
with open("score.txt", "w") as sc:
    sc.write(str(points))
print("Your point is ",points)
