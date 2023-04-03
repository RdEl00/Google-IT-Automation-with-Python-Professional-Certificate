# Loops

In this module you'll explore the intricacies of loops in Python! You'll learn how to use while loops to continuously execute code, as well as how to identify infinite loop errors and how to fix them. You'll also learn to use for loops to iterate over data, and how to use the range() function with for loops. You'll also explore common errors when using for loops and how to fix them.

## Learning Objectives

- Implement while loops to continuously execute code while a condition is true
- Identify and fix infinite loops when using while loops
- Utilize for loops to iterate over a block of code
- Use the range() function to control for loops
- Use nested while and for loops with if statements
- Identify and correct common errors when using loops


## Assessments

- [Practice Quiz - While Loops](#Practice-Quiz---While-Loops)
- [Practice Quiz - For Loops](#Practice-Quiz---For-Loops)
- [Practice Quiz - Recursion](#Practice-Quiz---Recursion)
- [Graded Assessment](#Graded-Assessment)

### Practice Quiz - While Loops

1. In Python, what do while loops do?  

> while loops tell the computer to repeatedly execute a set of instructions while a condition is true.

2. Which techniques can prevent an infinite while loop? Select all that apply.

> Change the value of a variable used in the while condition

> Use the break keyword

3. The following code contains an infinite loop, meaning the Python interpreter does not know when to exit the loop once the task is complete. To solve the problem, you will need to: 

    - Find the error in the code

    - Fix the while loop so there is an exit condition

*Hint: Try running your function with the number 0 as the input and observe the result.* 

Note that Coursera’s code blocks will time out after 5 seconds of running an infinite loop. If you get this timeout error message, it means the infinite loop has not been fixed.

```python
def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number % 2 == 0:
    number = number / 2
    if number == 0:
      break
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  

# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
```

4. Fill in the blanks to complete the while loop so that it returns the sum of all the divisors of a number, without including the number itself. As a reminder, a divisor is a number that divides into another without a remainder. To do this, you will need to:

    - Initialize the "divisor" and "total" variables with starting values

    - Complete the while loop condition

    - Increment the "divisor" variable inside the while loop

    - Complete the return statement

```python
# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.

def sum_divisors(number):
# Initialize the appropriate variables
  divisor = 1
  total = 0

  # Avoid dividing by 0 and negative numbers 
  # in the while loop by exiting the function
  # if "number" is less than one
  if number < 1:
    return 0 

  # Complete the while loop
  while divisor < number:
    if number % divisor == 0:
      total += divisor
    # Increment the correct variable
    divisor += 1

  # Return the correct variable 
  return total


print(sum_divisors(0)) # Should print 0
print(sum_divisors(3)) # Should print 1
# 1
print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# 114
```

5. Fill in the blanks to complete the function, which should output a multiplication table. The function accepts a variable “number” through its parameters. This “number” variable should be multiplied by the numbers 1 through 5, and printed in a format similar to “1x6=6” (“number” x “multiplier” = “result”). The code should also limit the “result” to not exceed 25. To satisfy these conditions, you will need to:

    - Initialize the “multiplier" variable with the starting value

    - Complete the while loop condition

    - Add an exit point for the loop

    - Increment the “multiplier" variable inside the while loop

```python
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier < 6:
        result = number * multiplier 
        if  result > 25 :
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15

multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24

```
[ :arrow_up: Back to top](#Loops)

### Practice Quiz - For Loops

1. How are while loops and for loops different in Python?

> While loops iterate while a condition is true, for loops iterate through a sequence of elements.

2. Which option would fix this for loop to print the numbers 12, 18, 24, 30, 36?

```python
for n in range(6,18+1,3):
    print(n*2)
```

3. Which for loops will print all even numbers from 0 to 18? Select all that apply.

```python
for n in range(19):
    if n % 2 == 0:
        print(n)
```
```python
for n in range(10):
    print(n+n)
```
4. Fill in the blanks so that the for loop will print the first 10 cube numbers (x**3) in a range that starts with x=1 and ends with x=10.

```python
for x in range(1,11):
  print(x**3)
```
5. Write a for loop with a three parameter range() function that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7. 

```python
for x in range(0, 101):
    if x % 7 == 0:
        print(x)
```

[ :arrow_up: Back to top](#Loops)

### Practice Quiz - Recursion

1. What is recursion used for?

> Recursion is used to call a function from inside the same function.

2. Which of these activities are good use cases for recursive programs? Check all that apply.

> Going through a file system collecting information related to directories and files.

> Managing permissions assigned to groups inside a company, when each group can contain both subgroups and users.

3. Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.

```python
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  number = number / base
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
```
4. The count_users function recursively counts the amount of users that belong to a group in the company system, by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members. But it has a bug! Can you spot the problem and fix it?

```python
def count_users(group):
  count = 0
  for member in get_members(group):
    if is_group(member):
      count += count_users(member)
    else:
      count += 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18
```
5. Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

```python
def sum_positive_numbers(n):
  if n == 1:
    return 1
  return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
```

[ :arrow_up: Back to top](#Loops)

### Graded Assessment

1. Fill in the blanks to print the numbers 1 through 7.

```python
number = 1 # Initialize the variable
while number < 8: # Complete the while loop condition
    print(number, end=" ")
    number += 1 # Increment the variable

# Should print 1 2 3 4 5 6 7 
```

2. Find and correct the error in the for loop below.  The loop should print every even number from 2 to 12.

```python
for number in range(2,13,2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12
```

3. Fill in the blanks to complete the function “even_numbers(n)”. This function should count how many even numbers exist in a sequence from 0 to the given “n”number, where 0 counts as an even number.  For example, even_numbers(25) should return 13, and even_numbers(6) should return 4.

```python
def even_numbers(n):
    count = 0
    current_number = 0
    while current_number < n+1: # Complete the while loop condition
        if current_number % 2 == 0:
            count += 1 # Increment the appropriate variable
        current_number += 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1
```
4. Fill in the blanks to complete the “rows_asterisks” function. This function should print rows of asterisks (*), where the number of rows is equal to the “rows” variable. The number of asterisks per row should correspond to the row number (row 1 should have 1 asterisk, row 2 should have 2 asterisks, etc.). Complete the code so that “row_asterisks(5)” will print:

```python
*
* *
* * *
* * * *
* * * * *
```

```python
def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(1, rows+1): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()

rows_asterisks(5)
# Should print the asterisk rows shown above

```

5. Fill in the blanks to complete the “counter” function. This function should count down from the “start” to “stop” variables when “start” is bigger than “stop”. Otherwise, it should count up from “start” to “stop”. Complete the code so that a function call like “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”.

```python
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop: # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            start -= 1 # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while start <= stop: # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            start += 1 # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
```

6. Fill in the blanks to complete the “all_numbers” function. This function should return a space-separated string of all numbers, from the starting   “minimum” variable  up to and including the “maximum” variable that's passed into the function. Complete the for loop so that a function call like “all_numbers(3,6)” will return the numbers “3 4 5 6”. 

```python
def all_numbers(minimum, maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # numbers up to and including the "maximum" value.
    for nbr in range(minimum, maximum+1): 

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string += str(nbr)
        return_string += " " 

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2,6))  # Should be 2 3 4 5 6
print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1,1)) # Should be -1 0 1
print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
print(all_numbers(0,0))  # Should be 0
```
7. The following code is supposed to add together all numbers from x to 10.  The code is returning an incorrect answer, what is the reason for this?

```python
x = 1
sum = 5
while x <= 10:
    sum += x
    x += 1
print(sum)
# Should print 55
```

> The "sum" variable is initialized with the wrong value

8. How many numbers will this loop print?  Your answer should be only one number.

> 5

9. What is the initial value of  the “outer_loop” variable on the first iteration of the nested "inner_loop"? Your answer should be only one number.

```python
for outer_loop in range(2, 6+1):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)
```

> 2

10. The following code causes an infinite loop. Can you figure out what is incorrect?

```python
def test_code(num):
  x = num
  while x % 2 == 0:
    x = x / 2

test_code(0)
```

> When called with 0, it triggers an infinite loop

[ :arrow_up: Back to top](#Loops)