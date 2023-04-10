# Strings, Lists and Dictionaries

In this module you'll dive into more advanced ways to manipulate strings using indexing, slicing, and advanced formatting. You'll also explore the more advanced data types: lists, tuples, and dictionaries. You'll learn to store, reference, and manipulate data in these structures, as well as combine them to store complex data structures.

## Learning Objectives

- Manipulate strings using indexing, slicing, and formatting
- Use lists and tuples to store, reference, and manipulate data
- Leverage dictionaries to store more complex data, reference data by keys, and manipulate data stored
- Combine the String, List, and Dictionary data types to construct complex data structures


## Assessments

- [Practice Quiz - Strings](#Practice-Quiz---Strings)
- [Practice Quiz - Lists](#Practice-Quiz---Lists)
- [Practice Quiz - Dictionaries](#Practice-Quiz---Dictionaries)
- [Graded Assessment](#Graded-Assessment)


### Practice Quiz - Strings

1. Fill in the blanks to complete the is_palindrome function. This function checks if a given string is a palindrome. A palindrome is a string that contains the same letters in the same order, whether the word is read from left to right or right to left. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". The function should ignore blank spaces and capitalization when checking if the given string is a palindrome. Complete this function to return True if the passed string is a palindrome, False if not. 

```python
def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:

        # The if-statement checks if the "letter" is not a space.
        if letter != " ":

            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string += letter
            reverse_string = letter + reverse_string

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code. 
    if new_string.lower() == reverse_string.lower():

        # If True, the "input_string" contains a palindrome.
        return True
		
    # Otherwise, return False.
    return False
	

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
```

2. Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".

```python
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
```

3. If we have a string variable named Weather = "Rainfall", which of the following will print the substring "Rain" or all characters before the "f"?

> print(Weather[:4])

4. Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."

```python
def nametag(first_name, last_name):
	return("{} {:.1s}.".format(first_name, last_name))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 
```

5. The replace_ending function replaces a specified substring at the end of a given sentence with a new substring. If the specified substring does not appear at the end of the given sentence, no action is performed and the original sentence is returned. If there is more than one occurrence of the specified substring in the sentence, only the substring at the end of the sentence is replaced. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).  

```python
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if old in sentence[-len(old):]:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence.rindex(old)
		new_sentence = sentence[:i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

```

[ :arrow_up: Back to top](#Strings-Lists-and-Dictionaries)

### Practice Quiz - Lists

1. Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

```python
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = []
for file in filenames:
    if ".hpp" in file:
        swp = file.replace(".hpp", ".h")
        newfilenames.append(swp)
    else:
        newfilenames.append(file)



print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
```

2. Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

```python
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  new_words = []
  for word in words:
    # Create the pig latin word and add it to the list
    end_p = word[1:] + word[0]
    end_ay = end_p + "ay"
    new_words.append(end_ay)
    say = " ".join(new_words)
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
```

3. The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
 For example: 
 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
 Fill in the blanks to make the code convert a permission in octal format into a string format.
 
 ```python
 def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for d in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if d >= value:
                result += letter
                d -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
 ```

4. Tuples and lists are very similar types of sequences. What is the main thing that makes a tuple different from a list?

> A tuple is immutable

5. The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

```python
def group_list(group, users):
  users1 = ", ".join(users)
  members = f"{group}: {users1}"
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
```

6. The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that. 

```python
def guest_list(guests):
	for guest in guests:
		name = guest[0]
		age = guest[1]
		profession = guest[2]
		print("{} is {} years old and works as {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
```

[ :arrow_up: Back to top](#Strings-Lists-and-Dictionaries)

### Practice Quiz - Dictionaries

1. The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

```python
def email_list(domains):
	emails = []
	for key, users in domains.items():
	  for user in users:
	    emails.append(user + "@" + key)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
```

2. The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.

```python
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			user_groups[user] = []
			if user not in user_groups:
				user_groups[user] = group
			else:
				user_groups[user].append(group)

	return(user_groups)


def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
```
3. The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries are replaced and new entries are added. What is the content of the dictionary “wardrobe“ at the end of the following code?

```python
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
```

> {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}

4. What’s a major advantage of using dictionaries over lists?

> It’s quicker and easier to find a specific element in a dictionary

5. The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.

```python
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

```

[ :arrow_up: Back to top](#Strings-Lists-and-Dictionaries)

### Graded Assessment

1. Fill in the blanks to complete the “confirm_length” function. This function should return how many characters a string contains as long as it has one or more characters, otherwise it will return 0. Complete the string operations needed in this function so that input like "Monday" will produce the output "6".

```python
def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word) != 0:
        # Complete the return statement using a string operation.
        return len(word) 
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0
```
2. Fill in the blank to complete the “string_words” function. This function should split up the words in the given “string” and return the number of words in the “string”.  Complete the string operation and method needed in this function so that a function call like "string_words("Hello, World")" will return the output "2".

```python
def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4
```

3. Consider the following scenario about using Python lists: 

Employees at a company shared  the distance they drive to work (in miles) through an online survey. These distances were automatically added by Python to a list called “distances” in the order that each employee submitted their distance. Management wants the list to be sorted in the order of the longest distance to the shortest distance. 

Complete the function to sort the “distances” list. This function should:

- sort the given “distances” list, passed through the function’s parameters; ; 

- reverse the sort order so that it goes from the longest to the shortest distance;

- return the modified “distances” list.

```python
def sort_distance(distances):
    distances.sort(reverse=True) # Sort the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]
```

4. Fill in the blank to complete the “squares” function. This function should use a list comprehension to create a list of squared numbers (using either the expression n*n or n**2). The function receives two variables and should return the list of squares that occur between the “start” and “end” variables inclusively (meaning the range should include both the “start” and “end” values). Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 9]”.

```python
def squares(start, end):
    return [ x**2 for x in range(start, end+1) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

5. Fill in the blanks to complete the “car_listing” function. This function accepts a “car_prices” dictionary. It should iterate through the keys (car models) and values (car prices) in that dictionary. For each item pair, the function should format a string so that a dictionary entry like ““Kia Soul“:19000” will print "A Kia Soul costs 19000 dollars". Each new string should appear on its own line.

```python
def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for key, value in car_prices.items():
    result += f" A {key} costs {value} dollars\n" # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars
```

6. Consider the following scenario about using Python dictionaries: 

Tessa and Rick are hosting a party. Together, they sent out invitations, and collected the responses in a dictionary, with names of their friends and the number of guests each friend will be bringing. 

Complete the function so that the “check_guests” function retrieves the number of guests (value)  the specified friend “guest” (key) is bringing. This function should:

- accept a dictionary “guest_list” and a key “guest” variable passed through the function parameters;

- print the values associated with the key variable.

```python
def check_guests(guest_list, guest):
  return guest_list[guest] # Return the value for the given key


guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2
```

7. Consider the following scenario about using Python dictionaries:

A teacher is using a dictionary to store student grades. The grades are stored as a point value out of 100.  Currently, the teacher has a dictionary setup for Term 1 grades and wants to duplicate it for Term 2. The student name keys in the dictionary should stay the same, but the grade values should be reset to 0.

Complete the “setup_gradebook” function so that input like “{"James": 93, "Felicity": 98, "Barakaa": 80}” will produce a resulting dictionary that contains  “{"James": 0, "Felicity": 0, "Barakaa": 0}”. This function should: 

- accept a dictionary “old_gradebook” variable through the function’s parameters;

- make a copy of the “old_gradebook” dictionary;

- iterate over each key and value pair in the new dictionary;

- replace the value for each key with the number 0;

- return the new dictionary.

```python
def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
  new_gradebook = old_gradebook.copy()
  print(new_gradebook) 
    # Complete the for loop to iterate over the new gradebook. 
  for key, value in new_gradebook.items():
     # Use a dictionary operation to reset the grade values to 0.
    value = 0
    new_gradebook.update({key:value})
  return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}

```

8. What do the following commands return when genre = "transcendental"?

```python
print(genre[:-8])
print(genre[-7:9])
```

> transc, nd

9. What does the list "music_genres" contain after these commands are executed?

```python
music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
```

> ['rock', 'pop', 'country', 'blues']

10. What do the following commands return?

```python
speed_limits = {"street": 35, "highway": 65, "school": 15}
speed_limits["highway"]
```

> 65

[ :arrow_up: Back to top](#Strings-Lists-and-Dictionaries) 
