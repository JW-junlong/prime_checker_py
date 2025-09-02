# imports from global libraries

# main variables


def value_validation(user_value):

    """
    Validates that the user input is numerical (int or float),
    will continue to prompt user for a new value until a numeric value is provided

    Parameters:
    user_value - initial value to be validated 

    returns:
    user_value - validated numerical value
    """

    # pseudocode:
    # runs a boolean checker that when failed, will repeat the loop
    # test if a converted float value equals to the given value, if yes, checker turns true and passes test, breaking loop
    # if not, checker remains false, request a new value from user and continues loop.

    # loops request until user enters any numerical value
    pass_fail = False
    while not pass_fail:
        try: 
            test_one = user_value
            test_one = float(user_value)
        except ValueError:
            print("Invalid value detected, please enter a numerical value! ")
            user_value = input("Enter new value: ")
        else:
            pass_fail = True

    return user_value


# run code
def main():

    value = input("please enter a value (type quit to exit program): ")
    # checks if user's value is a numerical value
    affirmed_value = value_validation(value)

main()