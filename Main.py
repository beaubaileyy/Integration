# Beau Bailey
# This program will be a useful resource that includes all of the programming
# Exercises and code that I have worked on in module resources.
"""This is the main file within the document that prompts the user to learn
about different types of python problems. __author__ = Beau Bailey."""

# This created function defines the function 'getSmaller' which finds the
# smaller of 2 user inputted numbers


def getSmaller(get_smaller_num1, get_smaller_num2):
    """Finds the smaller of two numbers entered by user. Returns smaller
    number."""
    if get_smaller_num1 < get_smaller_num2:
        smaller_num = get_smaller_num1
    else:
        smaller_num = get_smaller_num2
    return smaller_num


def smaller():
    """Prompts the user for 2 numbers in order to find the smaller of the
    two. Prints smaller number."""
    print("Enter a number: ")
    get_smaller_user_input1 = inputNumber()
    print("Enter another number: ")
    get_smaller_user_input2 = inputNumber()

    smaller_num = getSmaller(get_smaller_user_input1, get_smaller_user_input2)
    print("The smaller of the two numbers is", smaller_num)


def inputNumber():
    """Makes sure the input by the user is a number. Returns user input"""
    while True:
        try:
            user_input = int(input())
        except ValueError:
            print("You didn't enter a number. Please try again.")
            continue
        else:
            return user_input


def main():
    """Main function including multiple problems."""

    print("Hello and welcome to my Integration Project program!")
    print("If you dont mind me asking, what's your name?")
    user_name = input("My name is: ")
    continue_program = True

    while continue_program:
        try:

            print("\nWhich of the following choices would you like to look "
                  "at " + user_name + '?')
            print("Please enter the whole number that corresponds to the "
                  "choice you would like to see.")
            print("1. A simple addition problem")
            print("2. A simple multiplication problem")
            print("3. More complex addition loop")
            print("4. Value returning function problem")
            print("5. Quit")
            user_choice = int(input())
        except ValueError:
            print("That wasn't a choice, try again.")
            continue
# Within this portion of code if the user types the whole number 1 it
# Prompts them for a couple numbers to complete an addition problem

        if user_choice == 1:

            while True:
                print("\nThis part of the program will prompt you to complete "
                      "a simple addition problem.")
                print("Complete the following addition problem!")
                print("Enter two numbers that add up to 10")
                print("Enter a number: ")
                first_add_number = inputNumber()
                print("Enter another number: ")
                second_add_number = inputNumber()
                add_num1 = int(first_add_number)
                add_num2 = int(second_add_number)
                add_num_sum = add_num1 + add_num2
                print("sum = ", add_num_sum)

                if add_num_sum == 10:
                    print("Correct! Nice job " + user_name + '!')
                    break
                else:
                    print("Please try again!")
                    continue


# Within this portion of code if the user types the whole number 2 it prompts
# The user for a couple numbers to complete an multiplication problem
        elif user_choice == 2:

            while True:
                print("\nThis part of the program will prompt you to complete "
                      "a simple multiplication problem.")
                print("Now lets try it.\nEnter two numbers that multiply to "
                      "10")
                print("Enter first number: ")
                first_mult_number = inputNumber()
                print("Enter next number: ")
                second_mult_number = inputNumber()
                mult_num1 = int(first_mult_number)
                mult_num2 = int(second_mult_number)
                mult_num_product = mult_num1 * mult_num2
                if mult_num_product == 10:
                    print("Correct! Nice job " + user_name + '!')
                    break
                else:
                    print("Please try again!")
                    continue


# This part of the program prompts the user for a number over and over again
# Until the user enters '0' , once the user enters the specified input
# The sum will be printed
        elif user_choice == 3:

            print("\nThis part of the program will continually prompt you for "
                  "numbers and find the sum of them.")
            print("Once you would like to stop entering numbers, simply "
                  "input '0'")
            print("Then the program will print the sum of all the numbers "
                  "you entered.")
            addition_total = 0
            print("Enter a number: ")
            addition_number = inputNumber()

            while addition_number > 0 or addition_number < 0:
                addition_total = addition_total + addition_number
                print("Enter next number: ")
                addition_number = inputNumber()
            print("The total is: ", addition_total)


# This part of the program will prompt the user for 2 numbers and then prints
        # the larger of the 2 numbers
        elif user_choice == 4:
            print("\nThe following part of the program will prompt you to "
                  "enter 2 numbers.")
            print("It will then tell you which of the 2 numbers has the "
                  "smallest value.")
            print("This function uses the return function to set the call "
                  "value equal to what was returned.")

            smaller()


# If the user chooses the number '5' this ends the program and thanks the
        # user for running it
        elif user_choice == 5:
            print("\nThank you for checking my program out!")
            print("Have a good day", user_name + '!')
            break

        else:
            print("That wasn't an option. Please try again!")
            continue


main()
