# Basic Python Syntax

In this module you’ll learn about different data types in Python, how to identify them, and how to convert between them. You’ll also learn how to use variables to assign data and to reference variables. You’ll deep dive into functions: how to define them, pass them parameters, and have them return information. You’ll explore the concepts of code reuse, code style, and refactoring complex code, along with effectively using code comments. Finally, you’ll learn about comparing data using equality and logical operators, and leveraging these to build complex branching scripts using if statements.

## Learning Objectives

- Differentiate and convert between different data types utilizing variables
- Define and call functions utilizing parameters and return data
- Refactor code and write comments to reduce complexity and enhance code readability and code reuse
- Compare values using equality operators and logical operators
- Build complex branching scripts utilizing if, else and elif statements


## Assessments

- [Practice Quiz - Hello World](#Practice-Quiz---Hello-World)
- [Graded Assessment](#Graded-Assessment)


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