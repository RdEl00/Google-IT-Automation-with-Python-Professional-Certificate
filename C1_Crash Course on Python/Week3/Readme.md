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

[ :arrow_up: Back to top](#Loops)