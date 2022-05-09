#           CHAPTER 3: INTRODUCING LISTS
from operator import length_hint


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2].title())
print(bicycles[3].upper())
print(bicycles[-1])

# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time
names = ['Teniola', 'Ope', 'Favour', 'Joshua']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message should be
# the the same, but each message should be personalized with the
# person’s name.
names = ['Teniola', 'Ope', 'Favour', 'Joshua']
print(f'I love you, { names[0]}')
print(f'{names[1]}, omo Ibadan')
print(f'{names[2]}, what do I do with you?')
print(f'{names[3]}, alaya bi oke')

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
planes = ['Boeing', 'Falcon', 'Skyhawk', 'cessna']
print(f'{planes[-1].title()} are so cool, aren\'t they?')
planes.append('Blue Angels')
print(planes)

# appending, inserting("precise appending") and deleting from lists
motorcycle = []
motorcycle.append('Honda')
motorcycle.append('Yamaha')
motorcycle.append('Suzuki')

last_owned_motorcycle = motorcycle.pop()
print(f'I last owned a {last_owned_motorcycle}')

first_owned = motorcycle.pop(0)
print(f'the first motorbike I owned was a {first_owned}')

motorcycle.remove('Yamaha')
print(motorcycle)

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
guest_list = ['Noah Harari', 'Benedict Cumberbatch',
              'Zelensky', 'Bertrand Russell']
print(
    f'Hello, Professor {guest_list[0]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[1]}. You\'re especially welcome to my function')
print(
    f'Hello, President {guest_list[2]}. You\'re whole-heartedly to my function')
print(f'Hello, Sir {guest_list[3]}. You\'re whole-heartedly to my function')

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.
guest_list = ['Noah Harari', 'Benedict Cumberbatch',
              'Zelensky', 'Bertrand Russell']
print(guest_list[2])
del guest_list[2]
guest_list.insert(2, 'Teniola')
print(guest_list)
print(f'Hello, Mr. {guest_list[0]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[1]}. You\'re whole-heartedly to my function')
print(f'Hello, Miss {guest_list[2]}. You\'re whole-heartedly to my function')
print(f'Hello, Sir {guest_list[3]}. You\'re whole-heartedly to my function')

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.
guest_list = ['Noah Harari', 'Benedict Cumberbatch',
              'Zelensky', 'Bertrand Russell']
print(f'{guest_list}. Hello y\'all! I found a bigger dinner table so we would be having more guests.')
guest_list.insert(0, 'Bayo')
guest_list.insert(2, 'Kayode')
guest_list.append('Thor')
print(f'Hello, Mr. {guest_list[0]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[1]}. You\'re whole-heartedly to my function')
print(f'Hello, Miss {guest_list[2]}. You\'re whole-heartedly to my function')
print(f'Hello, Sir {guest_list[3]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[4]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[5]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[6]}. You\'re whole-heartedly to my function')

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.
guest_list = ['Noah Harari', 'Benedict Cumberbatch',
              'Zelensky', 'Bertrand Russell']
print(f'{guest_list}. Hello y\'all! I found a bigger dinner table so we would be having more guests.')
guest_list.insert(0, 'Bayo')
guest_list.insert(2, 'Kayode')
guest_list.append('Thor')
print(f'Hello, Mr. {guest_list[0]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[1]}. You\'re whole-heartedly to my function')
print(f'Hello, Miss {guest_list[2]}. You\'re whole-heartedly to my function')
print(f'Hello, Sir {guest_list[3]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[4]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[5]}. You\'re whole-heartedly to my function')
print(f'Hello, Mr. {guest_list[6]}. You\'re whole-heartedly to my function')

print('Sorry. I just found out I can only innvite two people for this dinner')

ejected_guest_1 = guest_list.pop(-1)
print(f'Sorry Mr. {ejected_guest_1}. You are disinvited')

ejected_guest_2 = guest_list.pop(-2)
print(f'Sorry Mr. {ejected_guest_2}. You are hereby disinvited')

ejected_guest_3 = guest_list.pop(-3)
print(f'Sorry Mr. {ejected_guest_3}. You are hereby disinvited')

ejected_guest_4 = guest_list.pop(-4)
print(f'Sorry Mr. {ejected_guest_4}. You are hereby disinvited')


# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']

# •	 Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']
print(location)

# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']
sorted(location)
print(sorted(location))

# •	 Show that your list is still in its original order by printing it.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']
print(location)

# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']
sorted(location, reverse=True)
print(location)
# •	 Show that your list is still in its original order by printing it again.

# •	 Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']
location.reverse()
print(location)
# •	 Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']
location.reverse()
print(location)
location.reverse()
print(location)

# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']
location.sort()
print(location)

# •	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
location = ['Berlin', 'Tokyo', 'Los Angeles', 'Victoria Island']
location.sort(reverse=True)
print(location)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.
guest_list = ['Noah Harari', 'Benedict Cumberbatch',
              'Zelensky', 'Bertrand Russell']
print(f'I am inviting {len(guest_list)} dignitaries to my dinner!')

# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
print(pets[0])
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
print(pets[-1])
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
print(pets[0].upper())
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
print(f'I love {pets[1]}  so much')
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
pets[0] = 'monkeys'
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
pets.append('monkeys')
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
pets.insert(0, 'monkeys')
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
del pets[0]
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
popped_item = pets.pop()
print(popped_item)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
omni = pets.pop(-2)
print(f'{omni} are omnivores')
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
pets.sort()
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
sorted(pets, reverse=True)
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
pets.sort(reverse=True)
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
pets.reverse()
print(pets)
#
pets = ['parrots', 'dogs', 'cats', 'pigs', 'ferrets']
pet_no = len(pets)
print(pet_no)
