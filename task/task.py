name = input("What is your name?")
chars = len(name)
print("Your name is " + name + " and that is " + str(chars) + " characters long!")

#Switch Contents in the glasses only using variable

glass1 = "milk"
glass2 = "juice"
print("Glass 1: " + glass1 + ". " + "Glass 2: " + glass2 + ".")

glass3 = glass1
glass1 = glass2
glass2 = glass3

print("Glass 1: " + glass1 + ". " + "Glass 2: " + glass2 + ".")