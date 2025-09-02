# imports from global libraries
import math

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


# quick check for any edge cases
def fast_check(user_value):

    """
    A set of checks which will rapidly determine edge cases
    Will return a true value if all tests are passed, or a false value if any tests are failed

    Parameters: 
    user_value - a validated integer value to be checked

    returns:
    true - when all tests are passed
    false - when any tests are failed
    """
    user_value = float(user_value)
    test_value = int(user_value)

    if user_value != test_value:
        return False
    elif user_value <= 2:
        return False
    else:
        return True

def checker(user_value, square_root):
    """
    Using rudimentary math, specifically trial division, determine if a number is prime by trying all integers 
    up to the square root value of the given user_value.

    Parameters:
    user_value - validated value
    square_root - the sqrt of user_value

    Returns:
    true - when all values except for the sqrt returns a mod operator value of > 0
    false - when any of the NON sqrt values return a mod operator value of 0
    """

    values_to_divide = int(square_root)
    largest_value = int(square_root)
    while values_to_divide > 1:
        if user_value % values_to_divide == 0:
            return False
        values_to_divide -= 1
    return True

def main():

    func_run = True
    while func_run:
        value = input("please enter a value (type quit to exit program): ")
        if value.lower() == "quit":
            func_run = False
            break
        else:
            # value validation:
            affirmed_value = value_validation(value)
            # rapid check:
            checked = fast_check(affirmed_value)
            # full check: (most basic method, will develop more as I learn the math behind them)
            if checked == True:
                affirmed_value = int(affirmed_value)
                square_root = math.sqrt(affirmed_value)
                checked = checker(affirmed_value, square_root)


            if checked == True:
                print("This value is a prime number! \n")
            else:
                print("This value is NOT a prime number \n")

    print("\n Thank you for trying my program! \n")

main()