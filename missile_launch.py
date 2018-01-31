import time
print("> /"+"*"*18 + "\\")
print(">>* MISSILE LAUNCH ***>")
print("> \\"+"*"*18 + "/")

name = "ALEXANDER PATRICK NACOL"
password = "BERNEPUGS"

name_guess = input("WHAT IS YOUR NAME? ").upper()
password_guess = input("WHAT IS THE PASSWORD? ").upper()

if name == name_guess and password == password_guess:
    print("MISSILE WILL LAUNCH IN 3")
    time.sleep(1)
    print("MISSILE WILL LAUNCH IN 2")
    time.sleep(1)
    print("MISSILE WILL LAUNCH IN 1")
    time.sleep(1)
    print("MISSILE LAUNCHED. ON THE WAY TO KOREA TO DESTROY KIM JONG UN")
else:
    print("SYSTEM WILL SELF DESTRUCT IN 3")
    time.sleep(1)
    print("SYSTEM WILL SELF DESTRUCT IN 2")
    time.sleep(1)
    print("SYSTEM WILL SELF DESTRUCT IN 1")
    time.sleep(1)
    print("BOOOOOM")
