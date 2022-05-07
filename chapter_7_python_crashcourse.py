# CHAPTER 7: USER INPUT AND WHILE LOOPS
#
# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”
message = input("what kind of car would you like?")
print(f"Let me see if I can find you a {message}")
#
#
# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
message = input("how many people are in your dinner group")
message = int(message)
if message > 8:
    print("We are sorry but you will have to wait for a table")
else:
    print("Your table is ready")
#
# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not
message = input("Give a number: ")
message = int(message)
if message % 10 == 0:
    print('your number is a multiple of 10')
else:
    print('your number ain\'t a multiple of 10')

# 7.4 Pizza Toppings:
# 	Write a loop that prompts the user to enter a series of pizza
# toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you'll add that topping to their pizza.
prompt = ("\nPLease enter a topping for your pizza")
prompt += ("\n(Enter 'quit' when you're finished entering toppings) ")

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.
prompt = input("what is your age?...")
prompt = int(prompt)

while prompt:
    if prompt < 3:
        print("You don't need to pay!")
    elif prompt >= 3 and prompt <= 12:
        print("The ticket costs $10")
    elif prompt > 12:
        print("The ticket costs $15")
    break

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
prompt = ("\nPLease enter a topping for your pizza")
prompt += ("\n(Enter 'quit' when you're finished entering toppings) ")

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza")
# •	 Use an active variable to control how long the loop runs.
prompt = ("\nPLease enter a topping for your pizza")
prompt += ("\n(Enter 'quit' when you're finished entering toppings) ")
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False

    else:
        print(f"I'll add {topping} to your pizza")

# •	 Use a break statement to exit the loop when the user enters a 'quit' value.
prompt = ("\nPLease enter a topping for your pizza")
prompt += ("\n(Enter 'quit' when you're finished entering toppings) ")

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza")

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# ctrl-C or close the window displaying the output.
#prompt = input("what is your age?...")
#prompt = int(prompt)
##
# while prompt:
#    if prompt < 3:
#        print("You don't need to pay!")
#    elif prompt >= 3 and prompt <= 12:
#        print("The ticket costs $10")
#    elif prompt > 12:
#        print("The ticket costs $15")


# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders = ['turkey', 'italian',  'blt', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    print("Making your sandwich...")
    current_sandwich = sandwich_orders.pop()
    print('I finished making your sandwich')
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
sandwich_orders = ['turkey', 'italian', 'blt', 'grilled cheese']
sandwich_orders.extend(['pastrami']*3)
finished_sandwiches = []
print("The restaurant has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    print("\nMaking your sandwich...")
    current_sandwich = sandwich_orders.pop()
    print('\tI finished making your sandwich\n')
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-10. Dream Vacation: Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

responses = {}


active = True
while active:
    prompt_user = "what is your name? "
    response = "If you could visit one place in the world, where would you go? "

    first_q = input(prompt_user)
    print(first_q)

    second_q = input(response)
    print(second_q)

    responses[first_q] = second_q

    repeat = "Would anyone else like to take this poll? (yes/no): "
    repeat = input(repeat)
    if repeat == "no" or repeat == "No":
        active = False

print("Showing results...\n")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}")
