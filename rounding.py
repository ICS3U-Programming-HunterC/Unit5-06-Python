#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 10, 2022
# This program asks what number you want rounded and then asks how many
# decimal places you want it rounded to and then displays it back to the user


def round_decimal(number, decimal):
    # round the number to the designated decimal place
    number[0] = number[0] * (10**decimal)
    number[0] += 0.5
    number[0] = int(number[0])
    number[0] = number[0] / (10**decimal)


def main():

    user_number = []

    try:
        # get the input
        temp_var1 = float(input("Enter a decimal number: "))
        user_decimal = int(input("Enter the number of decimal places: "))

        # append the first number so that it can be passed by reference
        user_number.append(temp_var1)

        # call the round_decimal function
        round_decimal(user_number, user_decimal)

        # display the outut
        print("{} rounded to {} is: {}".format(temp_var1, user_decimal, user_number[0]))

    except:
        print("Invalid input")


if __name__ == "__main__":
    main()
