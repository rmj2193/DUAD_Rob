def greet_user():
    #Prints a greeting, then calls another function
    print('Hello and Welcome to the program!')
    show_tip()  #Call the second function


def show_tip():
    #Prints a quick tip
    print("Tip: Please don't forget to comment your code!")

#Run the first function (which calls the second)
greet_user()