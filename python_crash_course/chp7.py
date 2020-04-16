print("Chapter 7 - User Input and While Loops")

number = input("Enter a number: ")
number = int(number)

while number > 0:
    print(number)
    number = number - 1

prompt = "Enter something and I will repeat: "
message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)    
        message = ""
    else:
        break
