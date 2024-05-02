price_of_house= 1000000
currency= "$"

user_input=input("Enter true if you have a good credit or false if you don't? ").lower()
if user_input== "true":
    print("Because you have a good credit, you are required to pay...")
    cal=str((price_of_house * 0.10 ))
    print("$" + cal)
elif user_input== "false":
    print('becase you  dont have a good credit, you are required to pay')
    cal=str((price_of_house * 0.20))
    print("$" + cal)
else:
    print('Enter true or false next time')
    print("Goodbye")
