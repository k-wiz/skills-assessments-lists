# SOLUTIONS!
# Note: Functions below assume that variables passed as arguments are valid.

def hello_world():
    """Prints "Hello World"."""

    print "Hello World"



def greeting(name):
    """Takes a name as a string and prints "Hi" followed by the name."""

    print "Hi", name



def multiply_two_nums (num1, num2):
    """ Takes two integers and multiplies them together. """

    total = num1 * num2
    return total



def print_string_x_times(sentence, num):
    """ Takes a string and an integer and prints the string that many times."""
    
    print sentence * num



def compare_to_zero(num):
    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    else:
        print "Zero"



def divisible_by_3(num):
    """ Takes an integer and returns a boolean (True or False), 
    depending on whether the number is evenly divisible by 3. """
    
    if num % 3 == 0:
        return True
    else:
        return False



def number_of_spaces(phrase):
    """" Takes a sentence as one string and returns the number of spaces. """

    count = 0
    for char in phrase:
        if char == " ":
            count += 1

    return count


def total_meal_cost(meal_price, tip=.15):
    """ Takes a meal price and tip percentage. Returns the total amount paid. 
    If no tip percentage is provided, defaults to .15 (15%). """

    total_amount_paid = meal_price + (meal_price * tip)

    return total_amount_paid



def sign_and_parity(num):
    """ Takes an integer and returns two pieces of information as strings 
    in a list -- "Positive" or "Negative" and "Even" or "Odd". """
    
    list_of_sign_and_parity = []

    if num > 0:
        list_of_sign_and_parity.append("Positive")
    elif num < 0:
        list_of_sign_and_parity.append("Negative")
    else:
        list_of_sign_and_parity.append("Neither")

    if num % 2 == 0:
        list_of_sign_and_parity.append("Even")
    elif num % 2 != 0:
        list_of_sign_and_parity.append("Odd")

    return list_of_sign_and_parity

# Calling function on number, unpacking what is returned into two variables. 
sign, parity = sign_and_parity(2)
print sign
print parity



def cost_with_tax(item_cost, state, tax=.05):
    """ Calculates total cost of item including tax based on state. 
    Assumes a tax rate of 7 percent in CA and 5 percent everywhere else. """

    if state == "CA":
        tax = .07

    total_cost = item_cost + (item_cost * tax)

    print total_cost
    return total_cost



def name_and_title(name, title):
    """ Prints name and corresponding job title. 
    If no title given, defaults to 'Engineer.'"""

    return title + " " + name




def print_letter(name, sender, title="Engineer"):
    """ Given a receiver's name, receiver's job title, and sender's name,
    prints a letter. """

    receiver = name_and_title(name, title)
    print "Dear {}, I think you are amazing! Sincerely, {}" .format(receiver, sender)



def append_num(num):
    """ Takes a number and appends it to the list numbers. """

    numbers = [1,2]
    numbers.append(num)







################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.


# 4. Write a function that takes a string and an integer and
#    prints the string that many times


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
