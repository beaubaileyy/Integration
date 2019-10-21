#Beau Bailey
#This program will be a useful resource that includes all of the programming exercises and code that I have worked on in module resources.


def main():

    print("Hello and welcome to my Integration Project program!")
    print("If you dont mind me asking, what's your name?")
    userName = input("My name is: ")
    continueProgram = True
    while continueProgram:
        print("Which of the following choices would you like to look at " + userName + '?')
        print("1. A simple addition problem")
        print("2. A simple multiplication problem")
        print("3. More complex addition loop")
        print("4. Value returning function problem")
        print("5. Quit")
        userChoice = int(input())

        if userChoice == 1:
            print("This part of the program will prompt you to complete a simple addition problem.")
            print("Complete the following addition problem!" )
            print("Enter two numbers that add up to 10")
            firstAddNumber = input("Enter a number: ")
            secondAddNumber = input("Enter another number: ")
            AddNum1 = int(firstAddNumber)
            AddNum2 = int(secondAddNumber)
            sum = AddNum1 + AddNum2
            print("sum = ", sum)
            if(sum == 10) : print("Correct! Nice job " + userName + '!')
            else: print("Please try again!")

        elif userChoice == 2:
            print("This part of the program will prompt you to complete a simple multiplication problem.")
            print("Now lets try it.\nEnter two numbers that multiply to 10")
            firstMultNumber = input("Enter a number: ")
            secondMultNumber = input("Enter another number: ")
            MultNum1 = int(firstMultNumber)
            MultNum2 = int(secondMultNumber)
            product = MultNum1 * MultNum2
            if(product == 10) : print("Correct! Nice job " + userName + '!')
            else: print("Please try again!")

        elif userChoice == 3:
            print("This part of the program will continually prompt you for positive numbers and find the sum of them.")
            print("Once you would like to stop entering numbers, simply input '0' or a negative number.")
            print("Then the program will print the sum of all the numbers you entered.")
            AdditionTotal = 0
            AdditionNumber = int(input("Enter first positive number:"))

            while AdditionNumber > 0 or AdditionNumber < 0:
                AdditionTotal = AdditionTotal + AdditionNumber
                AdditionNumber = int(input("Enter next number: "))
            print(AdditionTotal)
        elif userChoice == 4:
            print("The following part of the program will prompt you to enter 2 numbers.")
            print("It will then tell you which of the 2 numbers has the smallest value.")
            print("This function uses the return function to set the call value equal to what was returned.")
            def getSmaller(getSmallerNum1, getSmallerNum2):
                if getSmallerNum1 < getSmallerNum2:
                    smaller = getSmallerNum1
                else:
                    smaller = getSmallerNum2
                return smaller

            getSmallerUserInput1 = int(input("Enter a number: "))
            getSmallerUserInput2 = int(input("Enter a second number: "))

            smallerNumber = getSmaller(getSmallerUserInput1, getSmallerUserInput2)
            print("The Smaller of the two numbers is", smallerNumber)

        elif userChoice == 5:
            print("Thank you for checking my program out!")
            print("Have a good day", userName + '!')
            break

        else:
            print("That wasn't an option. Please try again!")
            continue
main()