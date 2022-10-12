master_pwd = input("What is the master password?: ")


def view():
    pass


def add():
    name = input('Account Name: ')
    pwd = input("password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("would you like to add a new password or view existing ones (view,Add)?,press q to quit").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
