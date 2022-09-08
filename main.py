print("Welcome to my Quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct')
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct')
    score += 1
else:
    print("Incorrect")

answer = input("What does ALU stand for? ")
if answer.lower() == "arithmetic and logic unit":
    print('correct')
    score += 1
else:
    print("Incorrect")

print("you got " + str(score) + " questions correct!")
print("you got " + str(score/3 * 100) + " %")
