import random
print("Guess The Number:-")
correct_answer = random.randint(0,1000)

guesscount = 0

while correct_answer<1000:
    n = int(input("Enter Your Guess:-"))
    guesscount+=1
    if n==correct_answer:
        print("Congo!! You guessed the number in ", guesscount, " try!")
        break
    

    elif n<correct_answer:
        print("Higher number please")
    else:
        print("Lower number please")
    
         


        

