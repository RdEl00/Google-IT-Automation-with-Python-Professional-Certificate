# Basic Python Syntax

In this module you’ll learn about different data types in Python, how to identify them, and how to convert between them. You’ll also learn how to use variables to assign data and to reference variables. You’ll deep dive into functions: how to define them, pass them parameters, and have them return information. You’ll explore the concepts of code reuse, code style, and refactoring complex code, along with effectively using code comments. Finally, you’ll learn about comparing data using equality and logical operators, and leveraging these to build complex branching scripts using if statements.

## Learning Objectives

- Differentiate and convert between different data types utilizing variables
- Define and call functions utilizing parameters and return data
- Refactor code and write comments to reduce complexity and enhance code readability and code reuse
- Compare values using equality operators and logical operators
- Build complex branching scripts utilizing if, else and elif statements


## Assessments

- [Practice Quiz - Expressions and Variables](#Practice-Quiz---Expressions-and-Variables)
- [Practice Quiz - Functions](#Practice-Quiz---Functions)
- [Graded Assessment](#Graded-Assessment)

### Practice Quiz - Expressions and Variables

1. In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.

```python
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total/2 
print("Each person needs to pay: " + str(share))
```

2. This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.

```python
numerator = 10
denominator = 10
result = numerator / denominator
print(int(result))
```

3. Combine the variables to display the sentence "How do you like Python so far?"

```python
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 +  " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7)
```

4. This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.

```python
print("2 + 2 = " + str((2 + 2)))
```

5. What do you call a combination of numbers, symbols, or other values that produce a result when evaluated?

> An expression

[ :arrow_up: Back to top](#Basic-Python-Syntax)

### Practice Quiz - Functions

1. This function converts miles to kilometers (km).
    - Complete the function to return the result of the conversion

    - Call the function to convert the trip distance from miles to kilometers

    - Fill in the blank to print the result of the conversion

    - Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

```python
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km * 2))
```
2. This function compares two numbers and returns them in increasing order.

    - Fill in the blanks, so the print statement displays the result of the function call in order.

*Hint: if a function returns multiple values, don't forget to store these values in multiple variables*

```python
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)
```

3. What are the values passed into functions as input called?

> Parameters

4. Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.

```python
def lucky_number(name):
  number = len(name) * 9
  msg = "Hello " + name + ". Your lucky number is " + str(number)
  return msg
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
```

5. What is the purpose of the def keyword?

> Used to define a new function

[ :arrow_up: Back to top](#Basic-Python-Syntax)

### Practice Quiz - Conditionals

1. What's the value of this Python expression: (2**2) == 4?

> True

2. Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".

```python
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
```

3. What’s the output of this code if number equals 10?

```python
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)
```
> 2

4. Is "A dog" smaller or larger than "A mouse"? Is 9999+8888 smaller or larger than 100*100? Replace the plus sign in the following code to let Python check it for you and then answer. 

```python
print("A dog" < "A mouse")
print(9999+8888 < 100*100)
```

> "A dog" is smaller than "A mouse" and 9999+8888 is larger than 100*100

5. If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?

```python
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size // filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder =  block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * 2
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
```

[ :arrow_up: Back to top](#Basic-Python-Syntax)

### Graded Assessment

1. Complete the code to output the statement, “192.168.1.10 is the IP address of Printer Server 1”. Remember that precise syntax must be used to receive credit.

```python
IP_address = "192.168.1.10"
host_name = "Printer Server 1"
print(IP_address + " is the IP address of " + host_name)
# Should print "192.168.1.10 is the IP address of Printer Server 1"
```

2. What’s the value of this Python expression: 7 < "number"?

> TypeError

3. What is the elif keyword used for?

> To handle more than two comparison cases

4. Consider the following scenario about using if-elif-else statements:

The fall weather is unpredictable.  If the temperature is below 32 degrees Fahrenheit, a heavy coat should be worn.  If it is above 32 degrees but not above 50 degrees, then a jacket should be sufficient.  If it is above 50 but not above 65 degrees, a sweatshirt is appropriate, and above 65 degrees a t-shirt can be worn.  

Fill in the blanks in the function below so it returns the proper clothing type for the temperature.

```python
def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"
    elif temp > 50:
        clothing = "Sweatshirt"
    elif temp > 32:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat
```

5. When using an if statement, the code inside the if block will only execute if the conditional statement returns what?

> True


6. Fill in the blanks to complete the function.  The character translator function receives a single lowercase letter, then prints the numeric location of the letter in the English alphabet.  For example, “a” would return 1 and “b” would return 2. Currently, this function only supports the letters “a”, “b”, “c”, and “d” It returns "unknown" for all other letters or if the letter is uppercase.

```python
def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown
```

7. Can you calculate the output of this code?

```python
def difference(x, y):
    z = x - y
    return z


print(difference(5, 3))
```

> 2

8. What's the value of this Python expression?

> False

9. Fill in the blanks to complete the “safe_division” function. The function accepts two numeric variables through the function parameters and divides the “numerator” by the “denominator”. The function’s main purpose is to prevent a ZeroDivisionError by checking if the “denominator” is 0. If it is 0, the function should return 0 instead of attempting the division. Otherwise all other numbers will be part of the division equation. Complete the body of the function so that the function completes its purpose. 

```python
def safe_division(numerator, denominator):
    # Complete the if block to catch any "denominator" variables
    # that are equal to 0.
    if denominator == 0:
        result = 0
    else:
        # Complete the division equation.
        result = numerator/denominator
    return result


print(safe_division(5, 5)) # Should print 1.0
print(safe_division(5, 4)) # Should print 1.25
print(safe_division(5, 0)) # Should print 0
print(safe_division(0, 5)) # Should print 0.0
```

10. Which of the following are good coding-style habits? Select all that apply.

> Adding comments

> Cleaning up duplicate code by creating a function that can be reused

 [ :arrow_up: Back to top](#Basic-Python-Syntax)