# CHAPTER 6: DICTIONARIES
# 6-1. Person: Use a dictionary to store information about a person you know.
sweetheart = {
    'first_name': 'teniola',
    'last_name': 'olaniyi',
    'age': 19,
    'city': 'lagos'
}

# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
sweetheart = {
    'first_name': 'teniola',
    'last_name': 'olaniyi',
    'age': 19,
    'city': 'lagos'
}
print(sweetheart['first_name'])
print(sweetheart.get('last_name'))
print(sweetheart.get('town', 'no value yet'))

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
fav_number = {
    'tobi': '7',
    'kunle': '10',
    'noah': '21',
    'solo': '1000',
    'ruth': '6',
}
print(fav_number['tobi'])
print(fav_number['kunle'])
print(fav_number['noah'])
print(fav_number['solo'])
print(fav_number['ruth'])


# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.
glossary = {
    'indentation': 'spaces on new lines to make code more readable',
    'loop': 'a code that acts repeatedly upon a set of values',
    'tab': 'usually equal to four spaces',
    'method': 'modifies a function',
    'argument': 'the values that a method can take',
}
# manual method
meaning = glossary['indentation']
print(f'indentation: {meaning}')
meaning = glossary['loop']
print(f'\nloop: {meaning}')
meaning = glossary['tab']
print(f'\ntab: {meaning}')
meaning = glossary['method']
print(f'\nmethod: {meaning}')
meaning = glossary['argument']
print(f'\nargument: {meaning}')

# looping method
for word, meaning in glossary.items():
    print(f'\nThe word "{word}" means "{meaning}".')

# example
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}  # dick

friends = ['phil', 'sarah']  # list
for name in favorite_languages.keys():  # every key in the dick is being assigned to the variable 'name'
    print(f'Hi, {name.title()}')

    if name in friends:
        # since 'name' is now key. This would call the values attached to the key
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}!')


# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.
glossary = {
    'indentation': 'spaces on new lines to make code more readable',
    'loop': 'a code that acts repeatedly upon a set of values',
    'tab': 'usually equal to four spaces',
    'method': 'modifies a function',
    'argument': 'the values that a method can take',
    'set': 'an unordered collection of items that must be unique'
}

for word, meaning in glossary.items():
    print(f'\nThe word "{word}" means "{meaning}".')

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
rivers = {
    'nigeria': 'niger',
    'usa': 'mississippi',
    'zambia': 'zambezi',
}
for river in rivers.values():
    print(f'\twho tf named {river.upper()}?!')

# •	 Use a loop to print the name of each river included in the dictionary.
rivers = {
    'nigeria': 'niger',
    'usa': 'mississippi',
    'zambia': 'zambezi',
}
for river in rivers.values():
    print(river)

# •	 Use a loop to print the name of each country included in the dictionary.
rivers = {
    'nigeria': 'niger',
    'usa': 'mississippi',
    'zambia': 'zambezi',
}
for river in rivers.keys():
    print(river)

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_takers = ['jen', 'mark']

# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_takers = ['jen', 'mark']
for name in favorite_languages.keys():
    if name in poll_takers:
        print(f'Thank you for responding, {name.title()}')
    if name not in poll_takers:
        print(f'Hey {name.upper()}! Pls come take the poll')

# SUMMARY: .item() returns the both key and value and variables have to be assigned to both
# .keys() (plural, not singular) returns the key
# .values (plural) returns the values
#
# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
sweetheart = {
    'first_name': 'teniola',
    'last_name': 'olaniyi',
    'age': 19,
    'city': 'lagos',
}

janitor = {
    'first_name': 'manor',
    'last_name': 'kelvin',
    'age': 35,
    'city': 'kano',
}

teacher = {
    'first_name': 'tayo',
    'last_name': 'ade',
    'age': 27,
    'city': 'abeokuta',
}

people = [sweetheart, janitor, teacher]
for person in people:
    name = person['first_name'].title() + ' ' + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(name + ', of ' + city + ', is ' + age + ' years old.')

# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.
sookie = {
    'species': 'cat',
    'color': 'calico',
    'owner': 'allie',
}
elsa = {
    'species': 'cat',
    'color': 'black',
    'owner': 'william',
}
ernie = {
    'species': 'dog',
    'color': 'tan',
    'owner': 'joe',
}

pets = []
pets.append(sookie)
pets.append(elsa)
pets.append(ernie)
# print(pets) : check

for pet in pets:
    animal = pet['species']
    color = pet['color']
    owner = pet['owner']
    print(f'This {animal} is of the colour {color} and its owner is {owner}')

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
favorite_places = {
    'william': ['lake tahoe', 'maldives', 'talmo'],
    'allie': ['talmo', 'mexico', 'bahamas'],
    'luke': ['home', 'nanas', 'grams'],
}
for name, value in favorite_places.items():
    print(
        f"{name.title()}'s favourite places are {value[0].title()}, {value[1].title()} and {value[2].title()} ")
# OR
favorite_places = {
    'william': ['lake tahoe', 'maldives', 'talmo'],
    'allie': ['talmo', 'mexico', 'bahamas'],
    'luke': ['home', 'nanas', 'grams'],
}
for name, value in favorite_places.items():
    print(f"\n{name}'s favourite places are:")
    for place in value:
        print(f"\t{place}")


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
fav_number = {
    'tobi': 7,
    'kunle': 10,
    'noah': 21,
    'solo': 1000,
    'ruth': 6,
}
fav_number['tobi'] = [7, 14, 28]
fav_number['kunle'] = [10, 20, 30]
fav_number['noah'] = [21, 21*2, 21*3]
print(fav_number)


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
    'atlanta': {
        'state': 'georgia',
        'population': 5500000,
        'fact': 'known as hotlanta',
    },
    'new york': {
        'state': 'new york',
        'population': 8500000,
        'fact': 'big apple',
    },
    'los angeles': {
        'state': 'california',
        'population': 4000000,
        'fact': 'city of angels',
    },
}

for city, city_dict in cities.items():
    state = city_dict['state']
    pop = city_dict['population']
    fact = city_dict['fact']

    print(f'{city.title()} of {state.title()} has a population of {pop} people and is known as "{fact}"')
# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.
