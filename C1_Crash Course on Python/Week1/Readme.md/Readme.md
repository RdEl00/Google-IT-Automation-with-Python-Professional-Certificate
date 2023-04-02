# Hello Python!

In this module we’ll introduce you to the Coursera platform and the course format. Then, we’ll dive into the basics of programming languages and syntax, as well as automation using scripting. We’ll also introduce you to the Python programming language and some of the benefits it offers. Last up, we’ll cover some basic functions and keywords of the language, along with some arithmetic operations.

## Learning Objectives
- Define the terms computer program, programming language, script, and automation
- Use the print() function to output data to the screen
- Explain the difference between the syntax and semantics of a programming language
- List some of the characteristics of the Python language
- Utilize basic Python arithmetic operators to obtain the results of mathematical expressions


## Assessments

- [Practice Quiz - Introduction to Programming](###Practice-Quiz---Introduction-to-Programming)
- [Practice Quiz - Introduction to Python](#Practice-Quiz---Introduction-to-Python)
- [Practice Quiz - Hello World](#Practice-Quiz---Hello-World)
- [Graded Assessment](#Graded-Assessment)



### Practice Quiz - Introduction to Programming

1. What’s a computer program?


> A list of instructions that the computer has to follow to reach a goal

2. What’s the syntax of a language?

> The rules of how to express things in that language

3. What’s the difference between a program and a script?


> There’s not much difference, but scripts are usually simpler and shorter.

4. Which of these scenarios are good candidates for automation? Select all that apply.


> Generating a sales report, split by region and product type

> Copying a file to all computers in a company

> Sending personalized emails to subscribers of your website

5. What are semantics when applied to programming code and pseudocode?

> The meaning of coded statements


### Practice Quiz - Introduction to Python

1. Fill in the correct Python command to put “My first Python program” onto the screen.

```python
print("My first Python program")
```

2. Python is an example of what type of programming language?

>  General purpose scripting language 

3. Convert this Bash command into Python:

```python
print("Have a nice day")
```

4. Fill in the correct Python commands to put “This is fun!” onto the screen 5 times. 

```python
for i in range(5):
  print("This is fun!")
```
5. Select the Python code snippet that corresponds to the following Javascript snippet:

```python
for i in range(10):
  print(i)
```

### Practice Quiz - Hello World

1. What are functions in Python?

> Functions are pieces of code that perform a unit of work.

2. What are keywords in Python?

> Keywords are reserved words that are used to construct instructions.

3. What does the print function do in Python?

> The print function outputs messages to the screen

4. Output a message that says "Programming in Python is fun!" to the screen.

```python
print("Programming in Python is fun!")
```

5. Replace the ___ placeholder and calculate the Golden ratio: 

```math
(1 + \sqrt{3})/2
```

*Tip: to calculate the square root of a number xx, you can use x**(1/2).*

```python
ratio = ((1+5**(1/2)))/2
print(ratio)
```
### Graded Assessment

1. What is a computer program?

> Step-by-step instructions on how to complete a set of tasks, to be executed by a computer.

2. Which of the following are true about programming languages? Select all that apply.

> Similar to human language, programming languages use syntax and semantics.

> Programming languages are used to write computer programs and scripts.

> Some common programming languages include Python, Java, C, C++, C#, and R.

3. What are some tasks that might be a good fit for full automation? Select all that apply.

> Detecting and removing duplicate data

> Updating specific files on multiple computers

4. What is the difference between syntax and semantics in a programming language?

> Syntax is a set of rules for how statements are constructed. Semantics refers to the intended meaning or effect of statements. 

5. Which of the following are characteristics of the Python language? Select all that apply.

> Python is cross-platform compatible

> Python is used in a wide variety of applications

6. Which Python function will output text, or other value, to the screen?

> print()

7. What should be the output of the expression below? 

```python
print(15+5+(3*2)/4**2+(3-7)*7)
```
> 
-7.625

8. Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days.  Print the result to the screen. Note: Your result should be in the format of just a number, not a sentence.

```python
# Enter code here:
print(86400 * 7)

# Should print 604800
```

9. Mercury has a diameter of approximately 1,516 miles.  Earth has a diameter of approximately 3,959 miles.  Use Python to calculate how much larger Earth’s diameter is than Mercury's (in miles). Note: Your result should be in the format of a number, not a sentence.

```python
# Enter code here:
print(3959 - 1516)

# Should print 2443
```