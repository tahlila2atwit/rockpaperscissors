import random
import time
print("You ready to play Rock Paper Scissors?")
x = input()
print("ok lets go")

b = ["Rock","Paper","Scissors"]


print('ROCK')
time.sleep(1)
print('PAPER')
time.sleep(1)
print('SCISSOR')
time.sleep(1)
print('SHOOT')

xx = input()

jaunt = ["You suck dawg", "man I could school you even if u cheat", "LOOOSEERRRR","Man terminate my program so ur sorry ass could go practice"]
loss = ["dam lets go again", "re run that", "one more time"]
t = ["u lucky",'haha i knew u was gonna do that','stop it']

computer = random.choice(b)
print(computer)

if computer == xx:
    print(random.choice(t))
elif (xx == "Rock" or "rock" and computer == "Scissors") or (xx == "Scissors" or "scissors" and computer == "Paper") or (xx == "Paper" or "paper" and computer == "Rock"):
    print(random.choice(loss))  
else:
    print(random.choice(jaunt))