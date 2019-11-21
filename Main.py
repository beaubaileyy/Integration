# Beau Bailey
# This program will be a useful resource that includes all of the programming
# Exercises and code that I have worked on in module resources.


def getSmaller(get_smaller_num1, get_smaller_num2):
    if get_smaller_num1 < get_smaller_num2:
        smaller_num = get_smaller_num1
    else:
        smaller_num = get_smaller_num2
    return smaller_num


def smaller():
    get_smaller_user_input1 = int(input("Enter a number: "))
    get_smaller_user_input2 = int(input("Enter a second number: "))

    smaller_num = getSmaller(get_smaller_user_input1, get_smaller_user_input2)
    print("The smaller of the two numbers is", smaller_num)


def main():

    print("Hello and welcome to my Integration Project program!")
    print("If you dont mind me asking, what's your name?")
    user_name = input("My name is: ")
    continue_program = True
    while continue_program:
        print("Which of the following choices would you like to look at " +
              user_name + '?')
        print("Please enter the whole number that corresponds to the choice "
              "you would like to see.")
        print("1. A simple addition problem")
        print("2. A simple multiplication problem")
        print("3. More complex addition loop")
        print("4. Value returning function problem")
        print("5. Quit")
        user_choice = int(input())


# Within this portion of code if the user types the whole number 1 it
# Prompts them for a couple numbers to complete an addition problem
        if user_choice == 1:
            print("This part of the program will prompt you to complete a "
                  "simple addition problem.")
            print("Complete the following addition problem!")
            print("Enter two numbers that add up to 10")
            first_add_number = input("Enter a number: ")
            second_add_number = input("Enter another number: ")
            add_num1 = int(first_add_number)
            add_num2 = int(second_add_number)
            add_num_sum = add_num1 + add_num2
            print("sum = ", add_num_sum)
            if sum == 10:
                print("Correct! Nice job " + user_name + '!')
            else:
                print("Please try again!")

# Within this portion of code if the user types the whole number 2 it prompts
# The user for a couple numbers to complete an multiplication problem
        elif user_choice == 2:
            print("This part of the program will prompt you to complete a "
                  "simple multiplication problem.")
            print("Now lets try it.\nEnter two numbers that multiply to 10")
            first_mult_number = input("Enter a number: ")
            second_mult_number = input("Enter another number: ")
            mult_num1 = int(first_mult_number)
            mult_num2 = int(second_mult_number)
            mult_num_product = mult_num1 * mult_num2
            if mult_num_product == 10:
                print("Correct! Nice job " + user_name + '!')
            else:
                print("Please try again!")

        elif user_choice == 3:
            print("This part of the program will continually prompt you for "
                  "positive numbers and find the sum of them.")
            print("Once you would like to stop entering numbers, simply "
                  "input '0' or a negative number.")
            print("Then the program will print the sum of all the numbers "
                  "you entered.")
            addition_total = 0
            addition_number = int(input("Enter first positive number:"))

            while addition_number > 0 or addition_number < 0:
                addition_total = addition_total + addition_number
                addition_number = int(input("Enter next number: "))
            print(addition_total)

        elif user_choice == 4:
            print("The following part of the program will prompt you to "
                  "enter 2 numbers.")
            print("It will then tell you which of the 2 numbers has the "
                  "smallest value.")
            print("This function uses the return function to set the call "
                  "value equal to what was returned.")

            smaller()

        elif user_choice == 5:
            print("Thank you for checking my program out!")
            print("Have a good day", user_name + '!')
            break

        else:
            print("That wasn't an option. Please try again!")
            continue


main()
