#
print("welcome to my first project")
spy_name = input("type your name")
print(spy_name)
salutation = input("what we call you(Mr. or mrs)?")
print("Alright" + salutation +"" + spy_name + "I'd like to know a little bit more about you...")
selection = input("does you want to continue (default or new) account")
if selection == "new":

     spy_name1 = input("enter new name")
    print(spy_name1)
    selection1 = input("what we call you(Mr. or mrs)?")
    print("Alright" + selection1+ "" + spy_name1 + "I'd like to know a little bit more about you...")

else
print("hello")