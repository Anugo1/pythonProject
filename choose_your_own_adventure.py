name = input("Type your name: ").upper()
print("Welcome", name, "to the adventure")

answer = input("" + name + " you are in a bus going to lagos,it spoils midway, Enter another bus or wait? ").lower()

if answer == "another":
    path1 = input("You don enter one chance bus o, grab the steering or jump out of the moving car?,Type grab to take "
                  " the steering or jump to jump out ").lower()

    if path1 == "grab":
        print("you caused an accident and everyone died including you")
    elif path1 == "jump":
        print("you sustained some minor injuries from the jump but survived and was saved.")
    else:
        print("choose from the options provided next time, you lose!")

elif answer == "wait":
    path2 = input("While waiting you got attacked by armed robbers,type give to give the money u have or fight to fight"
                  " them .").lower()
    if path2 == "give":
        print("they shoot you to hide their identity after you give them the money")
    elif path2 == "fight":
        print("you died while fighting them")

else:
    print("You must choose between the options provided next time!")
print("Thanks", name, "for trying ")
